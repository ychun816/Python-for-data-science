#!/usr/bin/env python3

import os
from typing import Iterable

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as plticker

from load_csv import load

# Dictionary to convert shorthand numbers (e.g., '1k', '2.5M', '3B') into integers
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


def render_plot(df_life_gdp: pd.DataFrame, year: str) -> None:
    """Render scatter plot of GDP vs Life Expectancy for a given year."""
    sns.set_theme()

    sc = sns.scatterplot(
        data=df_life_gdp,
        x="GDP",
        y="Life Expectancy",
        hue="Country",
        legend=False,
    )

    plt.title(f"{year}", fontsize=15)
    plt.xlabel("Gross domestic product", fontsize=10)
    plt.ylabel("Life Expectancy", fontsize=10)
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

    # Y-axis ticks explicitly requested by the user
    y_ticks = [20, 25, 30, 35, 40, 45, 50, 55]
    # Only keep ticks that fall within range
    min_y = df_life_gdp["Life Expectancy"].min()
    max_y = df_life_gdp["Life Expectancy"].max()
    y_ticks = [t for t in y_ticks if min_y <= t <= max_y]
    if y_ticks:
        sc.yaxis.set_major_locator(plticker.FixedLocator(y_ticks))

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


def gdp_life_expectancy(year: str) -> None:
    """Load CSVs, merge life expectancy and GDP for the given year, and plot."""
    abs_path = os.path.dirname(os.path.abspath(__file__))

    life_candidates = (
        os.path.join(abs_path, "../data/life_expectancy_years.csv"),
        os.path.join(abs_path, "../life_expectancy_years.csv"),
    )
    gdp_candidates = (
        os.path.join(abs_path, "../data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"),
        os.path.join(abs_path, "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"),
    )

    df_life = load(_first_existing(life_candidates))
    df_gdp = load(_first_existing(gdp_candidates))

    if df_life is None or df_gdp is None:
        raise RuntimeError("CSV data could not be loaded")

    # The CSVs in this exercise use year column names like '2010' (strings).
    if year not in df_life.columns or year not in df_gdp.columns:
        raise ValueError(f"{year} not found in dataset columns")

    df_life_sel = df_life[["country", year]].rename(columns={year: "Life Expectancy"})
    df_gdp_sel = df_gdp[["country", year]].rename(columns={year: "GDP"})

    df_merged = pd.merge(df_life_sel, df_gdp_sel, on="country", how="inner").dropna()

    # convert GDP to integer values
    df_merged["GDP"] = df_merged["GDP"].apply(_parse_gdp_value)
    df_merged["Country"] = df_merged["country"]

    render_plot(df_merged[["Country", "Life Expectancy", "GDP"]], year)

