
#! usr/bin/env python3

import os  # for file path operations
import pandas as pd  # for data manipulation

import seaborn as sns  # for plotting
from matplotlib import pyplot as plt  # for controlling figure and display
from matplotlib import ticker as plticker  # for custom tick int

from load_csv import load

# Dictionary to convert shorthand numbers (e.g., '1k', '2.5M', '3B') into integers
tens = dict(k=1e3, m=1e6, b=1e9)

#FORMAT
# Format x or y axis ticks into readable abbreviated numbers
def formater(value, tick) -> str:
    """
    Converts large numbers into human-readable form for plots.
    Examples:
    1000 -> '1.0k', 1500000 -> '1M', 2_500_000_000 -> '2.5B'
    """
    match value:
        case _ if value >= 1e9:
            return f'{value*1e-9:.1f}B'
        case _ if value >= 1e6:
            return f'{value*1e-6:.0f}M'
        case _ if value >= 1e3:
            return f'{value*1e-3:.1f}k'
        case _:
            return f'{value:.1f}'

#FIND INBETWEEN VALUES
# Find a good interval for axis ticks based on the range of values
def find_base(min_value:float, max_value:float) -> int:
    """
    Returns a sensible tick interval depending on the range.
    """
    range_value = max_value - min_value
    match range_value:
        case _ if range_value >= 2e5:
            return 50000
        case _ if range_value >= 1e5:
            return 20000
        case _ if range_value >= 5e4:
            return 10000
        case _ if range_value >= 1e4:
            return 5000
        case _:
            return 2000

#RENDER SCATTER SPOTS
# Render a scatterplot of GDP vs Life Expectancy
def render_plot(df_life_gdp: pd.DataFrame, year: str) -> None:
    """
    Uses seaborn and matplotlib to plot GDP vs Life Expectancy for all countries.
    """
    sns.set_theme()  # apply Seaborn styling

    # Scatterplot: x=GDP, y=Life Expectancy, color by Country
    sc = sns.scatterplot(
        data=df_life_gdp,
        x='GDP',
        y='Life Expectancy',
        hue='Country',
        legend=False
    )

    # Add plot title and axis labels
    plt.title(f'{year}', fontsize=15)
    # plt.title(f'Relation between GDP and life expectancy in {year}', fontsize=15)
    plt.xlabel('Gross domestic product', fontsize=10)
    plt.ylabel('Life Expectancy', fontsize=10)
    plt.tick_params(axis='both', labelsize=8)

    # Format x-axis ticks with human-readable numbers
    sc.xaxis.set_major_formatter(plt.FuncFormatter(formater))
    max_gdp = df_life_gdp['GDP'].max()
    min_gdp = df_life_gdp['GDP'].min()
    sc.xaxis.set_major_locator(plticker.MultipleLocator(find_base(min_gdp, max_gdp)))

    plt.show()  # display the plot


#PLOT THE WHOLE TABLE
# Main function: load data, clean, merge, plot
def gdp_life_expectancy(year: str) -> None:
    """
    Plot GDP vs Life Expectancy for all countries in a specific year.
    """
    try:
        abs_path = os.path.dirname(os.path.abspath(__file__))  # folder of current script

        # Load CSV files
        df_life = load(os.path.join(abs_path, "../data/life_expectancy_years.csv"))
        df_gdp = load(os.path.join(abs_path, "../data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))
        
        # Check if data successfully loaded
        if df_life is None or df_gdp is None:
            raise RuntimeError("CSV data could not be loaded")
        
        # Verify that the year exists in both datasets
        for df, name in zip([df_life, df_gdp], ["Life Expectancy", "GDP"]):
            if year not in df.columns:
                raise ValueError(f"{year} not found in {name} dataset")
        
        # Merge and clean data in one chain:
        # 1. Select only 'country' and the year column
        # 2. Rename the year column
        # 3. Merge datasets on country (inner join to keep only countries present in both)
        # 4. Drop rows with missing values
        # 5. Convert GDP strings like '1.2M' to integers using the unpack lambda
        df_life_gdp = (
            pd.merge(
                df_life[['country', year]].rename(columns={year: "Life Expectancy"}), 
                df_gdp[['country', year]].rename(columns={year: "GDP"}),
                on="country", 
                how="inner"
            )
            .dropna()
            .assign(
                GDP=lambda d: d["GDP"].apply(
                    lambda x: int(float(x[:-1])*tens[x[-1].lower()])
                    if isinstance(x, str) and x[-1].lower() in tens else int(x)
                ),
                Country=lambda d: d["country"]  # rename column for plotting
            )

        # Render the scatter plot
        render_plot(df_life_gdp[['Country', 'Life Expectancy', 'GDP']], year)


    except Exception as e:
        print(f"An error occurred in gdp_life_expectancy: {e}")
        raise













def life_expectancy(year:str): 
    """
    Placeholder function for life expectancy projections.

    Args:
        year (str): Year for projection.
    """
    try:



    