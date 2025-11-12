#!/usr/bin/env python3
# Shebang comment: file is executable with Python 3

import os  # Provides OS path and file operations
from typing import Iterable, Optional

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as plticker

from load_csv import load

# -------------------------------------------------------------------
# CONSTANTS AND HELPERS
# -------------------------------------------------------------------

# Mapping suffixes like 'k', 'm', 'b' to their numerical multipliers
tens = dict(k=1e3, m=1e6, b=1e9)


def formater(value, _tick) -> str:
    """Convert raw numeric tick values into human-friendly short form.

    Examples:
        1000 -> '1k', 1500000 -> '1M', 2500000000 -> '2.5B'
    """
    try:
        v = float(value)  # Convert to float for consistent scaling
    except Exception:
        return str(value)  # Fallback if not a number

    # Helper function to format with suffix, trimming '.0' if unnecessary
    def _fmt(val, suffix, decimals=1):
        s = f"{val:.{decimals}f}"
        if s.endswith('.0'):
            s = s[:-2]
        return f"{s}{suffix}"

    # Format according to magnitude
    if v >= 1e9:
        return _fmt(v / 1e9, 'B')
    if v >= 1e6:
        return _fmt(v / 1e6, 'M', decimals=0)
    if v >= 1e3:
        return _fmt(v / 1e3, 'k', decimals=0)
    if abs(v - round(v)) < 1e-6:
        return str(int(round(v)))  # Avoid '.0' for integers
    return f"{v:.1f}"


def find_base(min_value: float, max_value: float) -> int:
    """Choose a reasonable tick spacing depending on numeric range."""
    range_value = max_value - min_value
    if range_value >= 2e5:
        return 50000
    if range_value >= 1e5:
        return 20000
    if range_value >= 5e4:
        return 10000
    if range_value >= 1e4:
        return 5000
    return 2000


# -------------------------------------------------------------------
# PLOTTING FUNCTION
# -------------------------------------------------------------------

def render_plot(
    df_life_gdp: pd.DataFrame, year: str, save_path: Optional[str] = None
) -> None:
    """Draw scatter plot: GDP vs Life Expectancy for a given year.

    If save_path is specified → save the PNG file.
    If not → show interactively (useful for local testing).
    """
    sns.set_theme()  # Apply seaborn visual theme

    # Create scatter plot
    sc = sns.scatterplot(
        data=df_life_gdp,
        x="GDP",
        y="Life Expectancy",
        hue="Country",  # Color by country
        legend=False,   # Omit legend as requested
    )

    # Configure title and axis labels
    plt.title(f"{year}", fontsize=20, pad=12)
    plt.xlabel("Gross domestic product", fontsize=10)
    plt.ylabel("Life expantancy", fontsize=10)  # Matches required spelling
    plt.tick_params(axis="both", labelsize=8)

    # Apply number formatter to x-axis
    sc.xaxis.set_major_formatter(plt.FuncFormatter(formater))

    # Fixed X-axis ticks and limits (per exercise spec)
    x_ticks = [300, 1000, 10000]
    sc.xaxis.set_major_locator(plticker.FixedLocator(x_ticks))
    try:
        sc.set_xlim(300, 10000)
    except Exception:
        plt.xlim(300, 10000)

    # Fixed Y-axis ticks and limits (20 to 55 step 5)
    y_ticks = [20, 25, 30, 35, 40, 45, 50, 55]
    sc.yaxis.set_major_locator(plticker.FixedLocator(y_ticks))
    try:
        sc.set_ylim(min(y_ticks), max(y_ticks))
    except Exception:
        plt.ylim(min(y_ticks), max(y_ticks))

    # Save or display plot
    if save_path:
        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
    else:
        plt.show()


# -------------------------------------------------------------------
# CSV LOADING HELPERS
# -------------------------------------------------------------------

def _first_existing(candidates: Iterable[str]) -> str:
    """Return first path that exists among given candidates.

    If none exist, return the first candidate (so load() fails meaningfully).
    """
    for p in candidates:
        if os.path.exists(p):
            return p
    return list(candidates)[0]


def _parse_gdp_value(x):
    """Convert GDP shorthand (e.g. '2.5M', '3B') to integer."""
    if isinstance(x, str) and x:
        s = x.strip()
        last = s[-1].lower()
        if last in tens:
            try:
                return int(float(s[:-1]) * tens[last])
            except Exception:
                pass
        # Try parsing plain numeric string
        try:
            return int(float(s))
        except Exception:
            raise ValueError(f"Unable to parse GDP value: {x}")
    try:
        return int(x)
    except Exception:
        raise ValueError(f"Unable to parse GDP value: {x}")


# -------------------------------------------------------------------
# MAIN DATA HANDLING FUNCTION
# -------------------------------------------------------------------

def gdp_life_expectancy(year: str, save_path: Optional[str] = None) -> None:
    """Load and merge life expectancy + GDP CSVs for given year."""
    abs_path = os.path.dirname(os.path.abspath(__file__))

    # Potential file locations (different environments)
    life_candidates = (
        os.path.join(abs_path, "..", "data", "life_expectancy_years.csv"),
        os.path.join(abs_path, "..", "life_expectancy_years.csv"),
    )
    gdp_candidates = (
        os.path.join(
            abs_path,
            "..",
            "data",
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
        ),
        os.path.join(
            abs_path,
            "..",
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
        ),
    )

    # use load_csv.py
    def _call_loader(csv_path: str):
        """Use the local ex03 `load` function to read CSVs.

        The module already imports `load` from the sibling
        `load_csv.py` (ex03). Prefer that loader to ensure consistent
        behavior with this exercise's utilities.
        """
        return load(csv_path)

    # Load both datasets (life expectancy and GDP)
    df_life = _call_loader(_first_existing(life_candidates))
    df_gdp = _call_loader(_first_existing(gdp_candidates))

    # Extract raw pandas DataFrame if wrapped (DatasetView)
    if hasattr(df_life, "raw"):
        try:
            df_life = df_life.raw()
        except Exception:
            pass
    if hasattr(df_gdp, "raw"):
        try:
            df_gdp = df_gdp.raw()
        except Exception:
            pass

    if df_life is None or df_gdp is None:
        raise RuntimeError("CSV data could not be loaded")

    # Validate the requested year exists in both datasets
    if year not in df_life.columns or year not in df_gdp.columns:
        raise ValueError(f"{year} not found in dataset columns")

    # Select and rename relevant columns for clarity
    df_life_sel = df_life[["country", year]].rename(
        columns={year: "Life Expectancy"}
    )
    df_gdp_sel = df_gdp[["country", year]].rename(columns={year: "GDP"})

    # Merge the two datasets by country
    df_merged = pd.merge(
        df_life_sel, df_gdp_sel, on="country", how="inner"
    ).dropna()

    # Convert GDP values from shorthand to integers
    df_merged["GDP"] = df_merged["GDP"].apply(_parse_gdp_value)
    df_merged["Country"] = df_merged["country"]

    # Pass to plotting function
    render_plot(
        df_merged[["Country", "Life Expectancy", "GDP"]],
        year,
        save_path=save_path,
    )


# -------------------------------------------------------------------
# COMMAND LINE INTERFACE (CLI)
# -------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    def main() -> int:
        """CLI wrapper for `gdp_life_expectancy`.

        Parses command-line arguments and calls the plotting function.
        """
        p = argparse.ArgumentParser()
        p.add_argument("-y", "--year", default="1900", help="Year to plot")
        p.add_argument(
            "-o",
            "--output",
            default=None,
            help=(
                "Optional path to save plot as PNG. "
                "If not provided, a default path is used."
            ),
        )
        args = p.parse_args()

        # Default output path if user doesn’t specify one
        if not args.output:
            args.output = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                f"gdp_life_{args.year}.png",
            )

        try:
            gdp_life_expectancy(args.year, save_path=args.output)
            return 0
        except Exception as e:
            print("Error:", e)
            return 1

    # Ensure clean process exit code
    raise SystemExit(main())
