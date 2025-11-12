#!/usr/bin/env python3

import os
import re
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

from load_csv import load


def population_total(country: str, compare_country: str) -> None:
    """Compare population growth for two countries (1800-2050).

    Loads a cleaned CSV and saves a small plot file. Raises on
    missing data or load failures.
    """

    # 1) Load data
    path = os.path.join(
        os.path.dirname(__file__), "..", "data", "population_total.csv"
    )
    df = load(path)
    if df is None:
        raise RuntimeError(f"Could not load data from {path}")

    # If the loader returns a DatasetView (preview wrapper), extract the
    # underlying pandas DataFrame to allow column indexing.
    if hasattr(df, 'raw'):
        df = df.raw()

    # 2) Validate inputs
    countries = [country, compare_country]
    missing = [c for c in countries if c not in df["country"].values]
    if missing:
        raise ValueError(f"Country not found: {', '.join(missing)}")

    # 3) Keep only the two requested countries
    df = df[df["country"].isin(countries)]

    # 4) Helpers: convert '2.3M', '450k', etc., to integers
    tens = {"k": 1e3, "m": 1e6, "b": 1e9}

    def unpack(x):
        """Convert suffixed population strings to int.

        Returns an integer or raises on bad input.
        """
        if isinstance(x, (int, float)):
            return int(x)
        if not x:
            raise ValueError("Empty population value")
        s = str(x).strip()
        suffix = s[-1].lower()
        if suffix in tens:
            return int(float(s[:-1]) * tens[suffix])
        return int(float(s.replace(",", "")))

    # 5) Wide -> long and apply conversion
    df_long = (
        df.melt(id_vars="country", var_name="Year", value_name="Population")
        .assign(Population=lambda d: d["Population"].map(unpack))
        .dropna()
    )

    # 6) Keep only the requested year range and coerce types
    df_long = df_long[df_long["Year"].astype(int).between(1800, 2050)]
    df_long["Year"] = df_long["Year"].astype(int)

    # 7) Plot
    sns.set_theme()
    ax = sns.lineplot(data=df_long, x="Year", y="Population", hue="country")
    ax.set_title("Population Projections", fontsize=14)
    ax.set_xlabel("Year", fontsize=10)
    ax.set_ylabel("Population", fontsize=10)

    # X ticks and limits
    xticks = [1800, 1840, 1880, 1920, 1960, 2000, 2040]
    ax.set_xticks(xticks)
    ax.set_xlim(1800, 2050)
    ax.set_xticklabels([str(t) for t in xticks], rotation=0)

    # Y ticks: step in millions (20M) when possible
    try:
        y_step = 20_000_000
        ymin = int(df_long["Population"].min())
        ymax = int(df_long["Population"].max())
        ystart = max(0, (ymin // y_step) * y_step)
        yticks = np.arange(ystart, ymax + y_step, y_step)
        if yticks.size == 0:
            yticks = np.array([0, ymax])
        ax.set_yticks(yticks)
        from matplotlib.ticker import FuncFormatter

        def _millions(x, pos=None):
            return f"{int(round(x / 1e6))}M"

        ax.yaxis.set_major_formatter(FuncFormatter(_millions))
    except Exception:
        # If formatting fails, keep defaults
        pass

    # Save plot to a file (sanitized filename)
    def _sanitize(name: str) -> str:
        base = os.path.basename(name or "")
        sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", base)
        sanitized = sanitized.strip("._-")
        if not sanitized:
            import hashlib

            encoded = (name or "").encode("utf-8", errors="ignore")
            h = hashlib.sha1(encoded).hexdigest()[:8]
            sanitized = f"plot_{h}"
        return sanitized[:200]

    fname = (
        "population_"
        + _sanitize(country)
        + "_vs_"
        + _sanitize(compare_country)
        + ".png"
    )
    outpath = os.path.join(os.path.dirname(__file__), fname)
    plt.savefig(outpath, bbox_inches="tight")
    # print("Saved plot to", outpath)
    plt.close()


if __name__ == "__main__":
    import argparse

    def main() -> int:
        """CLI wrapper for `population_total`.

        Parses CLI arguments and calls the function. Exceptions are
        caught and reported; returns 0 on success, non-zero on error.
        """
        parser = argparse.ArgumentParser(
            description="Compare population for two countries (1800-2050)"
        )
        parser.add_argument("country", nargs="?", default="France")
        parser.add_argument("compare", nargs="?", default="Belgium")
        args = parser.parse_args()

        try:
            population_total(args.country, args.compare)
            return 0
        except Exception as e:
            print("Error:", e)
            return 1


    raise SystemExit(main())
