#! usr/bin/env python3

import sys
import os                     # for file path handling
import re
import numpy as np            # for array manipulation
import pandas as pd           # for DataFrame handling

from matplotlib import pyplot as plt # for plot
import seaborn as sns

# import seaborn as sns
# from matplotlib import pyplot as plt
# from matplotlib import ticker as plticker

from load_csv import load


def population_total(country:str, compare_country: str) -> None:
    """
    Compare population growth between two countries (1800–2050)
    using cleaned CSV data and plot results.

    Args:
        country (str): First country name.
        compare_country (str): Second country name.
    """

    # --- 1. Define file path & load data ---
    path = os.path.join(os.path.dirname(__file__), "../data/population_total.csv")
    df = load(path)

    if df is None:
        raise RuntimeError(f"Could not load data from {path}")

    # --- 2. Validate input countries ---
    countries = [country, compare_country]

    # List all countries requested that are not in the dataset.
    # check against values in the loaded dataframe's country column
    missing = [char for char in countries if char not in df["country"].values]
    if missing:
        raise ValueError(f"Country not found: {', '.join(missing)}")


    # --- 3. Filter data for both countries at once ---
    df = df[df["country"].isin(countries)] #returns Boolean Series (True if in countries). # df[...] → selects only rows where condition is True

    # --- 4. Define number unpacker for abbreviations ---
    # {}library (key: value) -> 1e3 → 1000, 1e6 → 1,000,000, 1e9 → 1,000,000,000.
    tens = {"k": 1e3, "m": 1e6, "b": 1e9}
    
    def unpack(x):
        """
        Convert population strings with suffixes to integers.
        Convert population strings with suffixes to integers.
        """
        # convert '2.3M' → 2_300_000, leave numeric as-is
        if isinstance(x, (int, float)):
            return int(x)
        if isinstance(x, str) and len(x) > 0:
            suffix = x[-1].lower()
            if suffix in tens:
                try:
                    return int(float(x[:-1]) * tens[suffix])
                except ValueError:
                    # fallback to numeric conversion if possible
                    return int(float(x.replace(',','').rstrip()))
            # no suffix, try plain numeric conversion after stripping commas
            return int(float(x.replace(',','')))
        # final fallback
        return int(x)

    # --- 5. Reshape: columns to long format ---
    df_long = (
        df.melt(id_vars="country", var_name="Year", value_name="Population")
          .assign(Population=lambda d: d["Population"].map(unpack))
          .dropna()
    )

    # --- 6. Keep only years 1800–2050 and ensure Year is numeric ---
    # convert Year to int for numeric plotting and set range 1800–2050
    df_long = df_long[df_long["Year"].astype(int).between(1800, 2050)]
    # now coerce the Year column to integers (important for numeric x-axis)
    df_long["Year"] = df_long["Year"].astype(int)

    # --- 7. Plot using Seaborn (delegated) ---
    sns.set_theme()
    ax = sns.lineplot(data=df_long, x="Year", y="Population", hue="country")
    ax.set_title(f"Population Projections", fontsize=14)
    ax.set_xlabel("Year", fontsize=10)
    ax.set_ylabel("Population", fontsize=10)

    # --- 8. Set ticks/formatting requested by user ---
    # X ticks: specific years
    xticks = [1800, 1840, 1880, 1920, 1960, 2000, 2040]
    ax.set_xticks(xticks)
    ax.set_xlim(1800, 2050)
    ax.set_xticklabels([str(t) for t in xticks], rotation=0)

    # Y ticks: 20M intervals, formatted as '20M', '40M', ...
    try:
        y_step = 20_000_000
        ymin = int(df_long["Population"].min())
        ymax = int(df_long["Population"].max())
        ystart = max(0, (ymin // y_step) * y_step)
        yticks = np.arange(ystart, ymax + y_step, y_step)
        if len(yticks) == 0:
            yticks = np.array([0, ymax])
        ax.set_yticks(yticks)
        from matplotlib.ticker import FuncFormatter

        def _millions(x, pos=None):
            return f"{int(round(x / 1e6))}M"

        ax.yaxis.set_major_formatter(FuncFormatter(_millions))
    except Exception:
        pass

    ################# to test display the graphics !!!! 
    # plt.show()
    # Save plot to a file (sanitized filename) so it can be viewed in headless environments
    def _sanitize(name: str) -> str:
        """Return a portable, short filename-friendly version of `name`.

        - Use basename to avoid embedded paths
        - Replace any run of unsafe chars with a single underscore
        - Allow letters, numbers, dot, underscore and hyphen
        - Strip leading/trailing separators
        - If result is empty, fall back to a short hash-based name
        """
        # avoid paths coming from user input
        base = os.path.basename(name or "")
        # replace runs of disallowed characters with a single underscore
        sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", base)
        sanitized = sanitized.strip("._-")
        if not sanitized:
            # short stable hash to avoid collisions and empty names
            import hashlib

            h = hashlib.sha1((name or "").encode("utf-8", errors="ignore")).hexdigest()[:8]
            sanitized = f"plot_{h}"
        # keep filename reasonably short
        return sanitized[:200]

    fname = f"population_{_sanitize(country)}_vs_{_sanitize(compare_country)}.png"
    outpath = os.path.join(os.path.dirname(__file__), fname)
    plt.savefig(outpath, bbox_inches="tight")
    print(f"Saved plot to {outpath}")
    plt.close()



### NOTES ### 

#     | Step                         | What It Does                                                  | Why It’s Efficient                                       |
# | ---------------------------- | ------------------------------------------------------------- | -------------------------------------------------------- |
# | **1. Load CSV once**         | Uses `os.path` for portability and a custom loader.           | Avoids hardcoding and keeps 42 style clean.              |
# | **2. Validate inputs**       | Checks if countries exist before any data work.               | Prevents wasted processing.                              |
# | **3. Filter early**          | Selects only two countries right away.                        | Keeps the dataframe small and memory-efficient.          |
# | **4. `unpack()` inline**     | Converts “2.3M”, “450k”, etc., to integers.                   | Self-contained, no need for a global lambda.             |
# | **5. `melt()` + `assign()`** | Turns wide data → long form + applies unpacking in one chain. | Pandas chaining is faster and cleaner than manual loops. |
# | **6. Year filtering**        | Keeps only relevant 1800–2050 range.                          | Avoids plotting noise.                                   |
# | **7. Plot inline**           | Uses seaborn defaults for styling.                            | Simple, modern, readable plotting.                       |


# df.melt() → wide → long format. Each year becomes a row.
# id_vars="country" → keep country as identifier.
# var_name="Year" → old column names become 'Year'.
# value_name="Population" → old values become 'Population'.
# .assign(Population=lambda d: d["Population"].map(unpack)) → apply unpack function to each value.
# .dropna() → remove missing values.

# sns.lineplot() → creates a line plot: x vs y, optionally grouped by hue.
# data=df_long → DataFrame to plot.
# hue="country" → different lines for each country.


##########