#!/usr/bin/env python3

import os
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as plticker

from load_csv import load


def life_expectancy(country: str) -> None:
    """
    Plot life expectancy for a given country from CSV data.
    """

    csv_path = os.path.join(
        os.path.dirname(__file__),
        'life_expectancy_years.csv',
    )
    data = load(csv_path)

    if data is None or country not in data['country'].values:
        raise ValueError(f"Country '{country}' not found in dataset.")

    country_data = data[data['country'] == country].drop(columns='country').T
    country_data.columns = ['Life Expectancy']
    country_data.index.name = 'Year'
    country_data.reset_index(inplace=True)

    country_data['Year'] = country_data['Year'].astype(int)
    _col = 'Life Expectancy'
    country_data[_col] = country_data[_col].astype(float)

    sns.set_theme()
    ax = sns.lineplot(data=country_data, x='Year', y='Life Expectancy')
    ax.set_title(f"{country} Life Expectancy Projections")
    ax.xaxis.set_major_locator(plticker.MultipleLocator(base=40))
    plt.show()
