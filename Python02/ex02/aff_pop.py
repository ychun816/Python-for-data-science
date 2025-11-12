#!/usr/bin/env python3

"""Plot population projections for two countries (1800–2050).

This module uses the `load` function from the sibling module
`load_csv.py` to read the dataset. It provides a single public
function `population_total(country, compare_country)` and a small CLI.
"""

# Future annotations for forward type hints (allows postponed eval)
from __future__ import annotations

import os       # for file and directory path operations
import re       # for sanitizing filenames using regular expressions
from typing import Optional  # for optional type hints (can be None)

import numpy as np  # numerical computations (e.g., creating tick ranges)
import seaborn as sns
from matplotlib import pyplot as plt

from load_csv import load  # custom CSV loader from your own module


def population_total(country: str, compare_country: str) -> None:
    """Compare population growth for two countries and save a PNG.

    This function loads population data (1800–2050) and plots a line
    graph comparing two countries. It expects a CSV file at:
        ../data/population_total.csv

    It relies on the `load()` function (from load_csv.py), which
    returns either:
      - a pandas DataFrame, or
      - a DatasetView wrapper with a `.raw()` method to get the DataFrame.
    """

    # Build the absolute path to the CSV file
    path = os.path.join(
        os.path.dirname(__file__), "..", "data", "population_total.csv"
    )

    # Load CSV using the shared load() utility
    df = load(path)
    if df is None:
        raise RuntimeError(f"Could not load data from {path}")

    # Some loaders (like DatasetView) wrap the DataFrame.
    # Extract the underlying DataFrame if `.raw()` is available.
    if hasattr(df, "raw"):
        df = df.raw()

    # Verify that both input countries exist in the dataset
    countries = [country, compare_country]
    missing = [c for c in countries if c not in df["country"].values]
    if missing:
        raise ValueError(f"Country not found: {', '.join(missing)}")

    # Filter only the two countries we want to compare
    df = df[df["country"].isin(countries)]

    # Map suffixes to multipliers: k=1e3, m=1e6, b=1e9
    multipliers = {"k": 1e3, "m": 1e6, "b": 1e9}

    # Helper: convert strings like "2.3M" or "450k" to int
    def _unpack(val: object) -> int:
        # Handle numeric values directly
        if isinstance(val, (int, float)):
            return int(val)
        # Handle missing or empty entries
        if val is None:
            raise ValueError("Empty population value")
        s = str(val).strip()
        if not s:
            raise ValueError("Empty population value")
        # Detect suffix and multiply accordingly
        last = s[-1].lower()
        if last in multipliers:
            return int(float(s[:-1]) * multipliers[last])
        # Otherwise, just clean commas and convert to int
        return int(float(s.replace(",", "")))

    # Convert wide format → long format
    # Example: columns for each year become rows (Year, Population)
    # Then, map() applies _unpack to clean population numbers.
    df_long = (
        df.melt(id_vars="country", var_name="Year", value_name="Population")
        .assign(Population=lambda d: d["Population"].map(_unpack))
        .dropna()
    )

    # Keep only rows where Year is between 1800–2050
    df_long = df_long[df_long["Year"].astype(int).between(1800, 2050)]
    df_long["Year"] = df_long["Year"].astype(int)

    # Configure seaborn visual theme for consistent styling
    sns.set_theme()

    # Create line plot comparing population trends of both countries
    ax = sns.lineplot(data=df_long, x="Year", y="Population", hue="country")

    # Add chart title and axis labels
    ax.set_title("Population Projections", fontsize=14)
    ax.set_xlabel("Year", fontsize=10)
    ax.set_ylabel("Population", fontsize=10)

    # Define X-axis ticks and formatting (every ~40 years)
    xticks = [1800, 1840, 1880, 1920, 1960, 2000, 2040]
    ax.set_xticks(xticks)
    ax.set_xlim(1800, 2050)
    ax.set_xticklabels([str(t) for t in xticks], rotation=0)

    # Try to set Y-axis ticks and label formatting in millions
    try:
        step = 20_000_000  # tick step size (20M)
        ymin = int(df_long["Population"].min())
        ymax = int(df_long["Population"].max())
        start = max(0, (ymin // step) * step)
        yticks = np.arange(start, ymax + step, step)
        if yticks.size == 0:
            yticks = np.array([0, ymax])
        ax.set_yticks(yticks)

        # Format tick labels to show in millions (e.g., "80M")
        from matplotlib.ticker import FuncFormatter

        def _fmt_millions(x, pos=None):
            return f"{int(round(x / 1e6))}M"

        ax.yaxis.set_major_formatter(FuncFormatter(_fmt_millions))
    except Exception:
        # If formatting fails (edge cases), fall back to defaults
        pass

    # Internal helper to create a safe filename for the output plot
    def _sanitize(name: Optional[str]) -> str:
        # Keep only safe characters: letters, digits, underscore, dot,
        # hyphen
        base = os.path.basename(name or "")
        sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", base)
        sanitized = sanitized.strip("._-")
        # If nothing left, fall back to a hashed name
        if not sanitized:
            import hashlib
            enc = (name or "").encode("utf-8", errors="ignore")
            h = hashlib.sha1(enc).hexdigest()[:8]
            sanitized = f"plot_{h}"
        return sanitized[:200]  # limit filename length for safety

    # Compose output filename
    fname = (
        "population_"
        + _sanitize(country)
        + "_vs_"
        + _sanitize(compare_country)
        + ".png"
    )

    # Save final plot into the same directory as this script
    outpath = os.path.join(os.path.dirname(__file__), fname)
    plt.savefig(outpath, bbox_inches="tight")  # Save with tight bounding box
    plt.close()  # Close the figure to free memory


def main() -> int:
    """Command-line interface (CLI) entry point.

    Parses arguments, calls population_total(), and returns an exit code.
    Returns:
        0  success
        1  failure (e.g., invalid country or file missing)
    """
    import argparse

    # Define command-line options
    parser = argparse.ArgumentParser(
        description="Compare population for two countries (1800–2050)"
    )
    # first country
    parser.add_argument("country", nargs="?", default="France")
    # second country
    parser.add_argument("compare", nargs="?", default="Belgium")
    args = parser.parse_args()

    # Execute plotting with error handling
    try:
        population_total(args.country, args.compare)
        return 0  # success
    except Exception as exc:
        print("Error:", exc)
        return 1  # failure


# When script is executed directly from command line
if __name__ == "__main__":
    # Call main() and exit with its return code
    raise SystemExit(main())
