#!/usr/bin/env python3

import importlib.util
import os
from typing import Iterable, Optional

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as plticker

from load_csv import load

# Convert shorthand numbers (e.g., '1k', '2.5M', '3B') to integers
tens = dict(k=1e3, m=1e6, b=1e9)


def formater(value, _tick) -> str:
    """Format tick values into human-friendly abbreviations.

    Examples:
        1000 -> '1.0k', 1500000 -> '1M', 2500000000 -> '2.5B'
    """
    try:
        v = float(value)
    except Exception:
        return str(value)

    # Helper to format scaled values without unnecessary '.0'
    def _fmt(val, suffix, decimals=1):
        s = f"{val:.{decimals}f}"
        if s.endswith('.0'):
            s = s[:-2]
        return f"{s}{suffix}"

    if v >= 1e9:
        return _fmt(v / 1e9, 'B')
    if v >= 1e6:
        return _fmt(v / 1e6, 'M', decimals=0)
    if v >= 1e3:
        # For thousands prefer no decimal when value is whole (1k, 10k)
        return _fmt(v / 1e3, 'k', decimals=0)

    # For small numbers, show integer when appropriate
    if abs(v - round(v)) < 1e-6:
        return str(int(round(v)))
    return f"{v:.1f}"


def find_base(min_value: float, max_value: float) -> int:
    """Choose a reasonable tick interval based on range size."""
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


def render_plot(
    df_life_gdp: pd.DataFrame, year: str, save_path: Optional[str] = None
) -> None:
    """Render scatter plot of GDP vs Life Expectancy for a given year.

    If save_path is provided the plot will be written to that file. If not,
    the plot will be shown interactively.
    """
    sns.set_theme()

    sc = sns.scatterplot(
        data=df_life_gdp,
        x="GDP",
        y="Life Expectancy",
        hue="Country",
        legend=False,
    )

    # Large, centered year-only title (matches requested style)
    plt.title(f"{year}", fontsize=20, pad=12)
    plt.xlabel("Gross domestic product", fontsize=10)
    # Use the exact Y label requested by the user
    plt.ylabel("Life expantancy", fontsize=10)
    plt.tick_params(axis="both", labelsize=8)

    sc.xaxis.set_major_formatter(plt.FuncFormatter(formater))

    # Set explicit x-range and ticks per user request: 300 -> 1k -> 10k
    x_ticks = [300, 1000, 10000]
    sc.xaxis.set_major_locator(plticker.FixedLocator(x_ticks))
    # Force x-limits to the requested range so ticks show consistently
    try:
        sc.set_xlim(300, 10000)
    except Exception:
        plt.xlim(300, 10000)

    # Y-axis ticks explicitly requested by the user (20..55 step 5)
    y_ticks = [20, 25, 30, 35, 40, 45, 50, 55]
    sc.yaxis.set_major_locator(plticker.FixedLocator(y_ticks))
    # Force y-limits so ticks are visible and match the requested range
    try:
        sc.set_ylim(min(y_ticks), max(y_ticks))
    except Exception:
        plt.ylim(min(y_ticks), max(y_ticks))

    # Legend intentionally omitted per user request

    if save_path:
        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        # print(f"Saved plot to {os.path.abspath(save_path)}")
    else:
        plt.show()


def _first_existing(candidates: Iterable[str]) -> str:
    for p in candidates:
        if os.path.exists(p):
            return p
    # return first candidate (so load will raise FileNotFoundError)
    return list(candidates)[0]


def _parse_gdp_value(x):
    if isinstance(x, str) and x:
        s = x.strip()
        last = s[-1].lower()
        if last in tens:
            try:
                return int(float(s[:-1]) * tens[last])
            except Exception:
                pass
        # try plain numeric string
        try:
            return int(float(s))
        except Exception:
            raise ValueError(f"Unable to parse GDP value: {x}")
    try:
        return int(x)
    except Exception:
        raise ValueError(f"Unable to parse GDP value: {x}")


def gdp_life_expectancy(year: str, save_path: Optional[str] = None) -> None:
    """Load CSVs, merge life expectancy and GDP for the given year."""
    abs_path = os.path.dirname(os.path.abspath(__file__))

    life_candidates = (
        os.path.join(
            abs_path,
            "..",
            "data",
            "life_expectancy_years.csv",
        ),
        os.path.join(
            abs_path,
            "..",
            "life_expectancy_years.csv",
        ),
    )
    gdp_candidates = (
        os.path.join(
            abs_path,
            "..",
            "data",
            (
                "income_per_person_gdppercapita_"
                "ppp_inflation_adjusted.csv"
            ),
        ),
        os.path.join(
            abs_path,
            "..",
            (
                "income_per_person_gdppercapita_"
                "ppp_inflation_adjusted.csv"
            ),
        ),
    )

    # Prefer the loader from ex02 if available (user request). Fall back to
    # the local `load` imported at module level.
    def _call_loader(csv_path: str):
        # candidate ex02 loader location
        ex02_loader = os.path.join(abs_path, "..", "ex02", "load_csv.py")
        if os.path.exists(ex02_loader):
            try:
                spec = importlib.util.spec_from_file_location(
                    "ex02_load_csv", ex02_loader
                )
                mod = importlib.util.module_from_spec(spec)
                assert spec and spec.loader
                spec.loader.exec_module(mod)  # type: ignore[attr-defined]
                if hasattr(mod, "load"):
                    return mod.load(csv_path)
            except Exception:
                # If anything fails, fall back to the default `load`.
                pass
        return load(csv_path)

    df_life = _call_loader(_first_existing(life_candidates))
    df_gdp = _call_loader(_first_existing(gdp_candidates))

    # If the loader returns a preview-wrapper (DatasetView) extract raw DF
    if hasattr(df_life, "raw"):
        try:
            df_life = df_life.raw()
        except Exception:
            # leave as-is; load() should have printed an error earlier
            pass
    if hasattr(df_gdp, "raw"):
        try:
            df_gdp = df_gdp.raw()
        except Exception:
            pass

    if df_life is None or df_gdp is None:
        raise RuntimeError("CSV data could not be loaded")

    # The CSVs in this exercise use year column names like '2010' (strings).
    if year not in df_life.columns or year not in df_gdp.columns:
        raise ValueError(f"{year} not found in dataset columns")

    df_life_sel = (
        df_life[["country", year]]
        .rename(columns={year: "Life Expectancy"})
    )
    df_gdp_sel = (
        df_gdp[["country", year]]
        .rename(columns={year: "GDP"})
    )

    df_merged = (
        pd.merge(df_life_sel, df_gdp_sel, on="country", how="inner")
        .dropna()
    )

    # convert GDP to integer values

    df_merged["GDP"] = df_merged["GDP"].apply(_parse_gdp_value)
    df_merged["Country"] = df_merged["country"]

    render_plot(
        df_merged[["Country", "Life Expectancy", "GDP"]],
        year,
        save_path=save_path,
    )


if __name__ == "__main__":
    # Default to year 1900 and save to a sensible filename when run directly.
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("-y", "--year", default="1900", help="Year to plot")
    p.add_argument(
        "-o",
        "--output",
        default=None,
        help=(
            "Optional path to save the plot as PNG. "
            "If omitted the plot is shown."
        ),
    )
    args = p.parse_args()

    # If no output path provided, save to a sensible default instead of
    # attempting an interactive display. This avoids silently not producing
    # a graphic in headless environments (CI, containers, remote shells).
    if not args.output:
        args.output = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            f"gdp_life_{args.year}.png",
        )

    gdp_life_expectancy(args.year, save_path=args.output)
