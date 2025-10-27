#! usr/bin/env python3

# The exercise explicitely states that the loaded file should be the life_expectancy_years.cvs. For this reason, any other file will be considered invalid, resulting in the function's behavior being undefined.

# life_expectancy(country:str)
# Parameters: country (str): takes a single parameter country, which is a string containing the name of the country.
# Return Value: none!

import sys
import os                     # for file path handling
import numpy as np            # for array manipulation
import pandas as pd           # for DataFrame handling
import seaborn as sns         # for plotting


from matplotlib import pyplot as plt
from matplotlib import ticker as plticker

from load_csv import load


def life_expectancy(country:str) -> None:
    """
    Plot life expectancy for a given country from CSV data.
    Returns None.
    """

    try:
        # Build the absolute path to the CSV file, relative to this script
        csv_path = os.path.join(os.path.dirname(__file__), 'life_expectancy_years.csv')


        # Load CSV file into a Pandas DataFrame using your custom load function
        data = load(csv_path)

        # If the DataFrame is None (failed load) or country is not in the dataset, raise an error
        if data is None or country not in data['country'].values:
            raise ValueError(f"Country '{country}' not found in dataset.")

        # Filter the DataFrame to only the row of the selected country
        # Drop the 'country' column and transpose (.T) so years become a column
        country_data = data[data['country'] == country].drop(columns='country').T

        # Rename the single column to 'Life Expectancy'
        # Set the index name to 'Year' for clarity
        # Reset the index so 'Year' becomes a proper column
        country_data.columns = ['Life Expectancy']
        country_data.index.name = 'Year'
        country_data.reset_index(inplace=True)

        # Convert the 'Year' column values from string to integer
        # Convert the 'Life Expectancy' column values from string/object to float
        country_data['Year'] = country_data['Year'].astype(int)
        country_data['Life Expectancy'] = country_data['Life Expectancy'].astype(float)        

        # Set the Seaborn theme for nicer plot styling
        sns.set_theme()

        # Create a line plot with 'Year' on x-axis and 'Life Expectancy' on y-axis
        ax = sns.lineplot(data=country_data, x='Year', y='Life Expectancy')
        
        # Add a plot title
        # Put a major tick every 40 years on the x-axis
        # Show the plot window
        ax.set_title(f"{country} Life Expectancy Projections")
        ax.xaxis.set_major_locator(plticker.MultipleLocator(base=40))
        plt.show()


    except Exception as e:
        raise RuntimeError(f"Runtime Error: {e}")



### NOTES ###

# | Function / Method / Operation                          | Library              | Usage / Purpose                                | Example / Notes                                        |
# | ------------------------------------------------------ | -------------------- | ---------------------------------------------- | ------------------------------------------------------ |
# | `os.path.dirname(__file__)`                            | os                   | Returns the directory path of the current file | Useful for building relative paths                     |
# | `os.path.join(a, b)`                                   | os                   | Joins paths in a platform-independent way      | `'folder' + 'file.csv'` → `'folder/file.csv'` on Linux |
# | `load(path)`                                           | custom               | Loads a CSV into a Pandas DataFrame            | Returns a DataFrame with CSV content                   |
# | `df['country'].values`                                 | pandas               | Access the underlying numpy array of a column  | Use to check if a value exists with `in`               |
# | `df[df['country'] == country]`                         | pandas               | Filters rows where column matches a value      | Returns a new DataFrame with only matching rows        |
# | `.drop(columns='country')`                             | pandas               | Remove one or more columns from DataFrame      | Useful to focus only on numeric columns for plotting   |
# | `.T`                                                   | pandas               | Transpose a DataFrame (swap rows and columns)  | Converts single row into column with index as years    |
# | `.columns = ['Life Expectancy']`                       | pandas               | Rename column(s)                               | Makes plot easier to understand                        |
# | `.index.name = 'Year'`                                 | pandas               | Give the index a name                          | Helps when resetting index for plotting                |
# | `.reset_index(inplace=True)`                           | pandas               | Converts index into a normal column            | Needed for Seaborn plotting with columns as x/y        |
# | `.astype(int)` / `.astype(float)`                      | pandas               | Convert data types                             | Ensures numeric types for plotting                     |
# | `sns.set_theme()`                                      | seaborn              | Set a default theme for plots                  | Changes style (background, colors) globally            |
# | `sns.lineplot(data=df, x='Year', y='Life Expectancy')` | seaborn              | Create a line chart                            | Returns an Axes object to customize further            |
# | `.set_title('title')`                                  | matplotlib / seaborn | Set the plot’s title                           | Can also adjust fontsize, fontweight                   |
# | `plticker.MultipleLocator(base=40)`                    | matplotlib.ticker    | Create ticks at fixed intervals                | base=40 → every 40 years                               |
# | `ax.xaxis.set_major_locator(locator)`                  | matplotlib           | Apply tick locator to x-axis                   | Control how often ticks appear                         |
# | `plt.show()`                                           | matplotlib.pyplot    | Display the figure                             | Blocks execution until window is closed                |
# | `try … except Exception as e`                          | Python built-in      | Handle errors safely                           | Useful to catch any runtime error                      |
# | `raise RuntimeError(f"...")`                           | Python built-in      | Re-throw an error with custom message          | Keeps program robust and debuggable                    |


####