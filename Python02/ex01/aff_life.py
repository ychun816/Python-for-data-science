#!/usr/bin/env python3

import os  # For working with file and directory paths
from load_csv import load  # local loader in ex01
import seaborn as sns  # For statistical data visualization
from matplotlib import pyplot as plt  # For creating plots and figures
from matplotlib import ticker as plticker  # For controlling axis ticks
from typing import Optional  # For optional type hints


# Note: we use the local `load_csv.load` from ex01 directly. That loader
# already knows how to resolve files in ../data and the exercise layout.

# -----------------------------------------------------------
# Note: we don’t import the loader immediately at the top level.
# Doing so could execute file I/O during import, which is bad practice.
# Instead, we call `_import_ex00_loader()` later at runtime when needed.
# -----------------------------------------------------------

# Do not import the ex00 loader at module import time. Obtaining the
# loader at import time can perform I/O and raise during import which
# violates the "no global code" rule. Call `_import_ex00_loader()` at
# runtime instead (see usage in `life_expectancy`).


def life_expectancy(
    country: str,
    save_path: Optional[str] = None,
    xticks: Optional[list] = None,
    yticks: Optional[list] = None,
    xlabel: Optional[str] = None,
    show_year_label: bool = False,
    year_label_pad: int = 15,
) -> None:
    """
    Plot life expectancy for a given country from CSV data.

    Parameters
    ----------
    country : str
        Name of the country to plot.
    save_path : str, optional
        Path to save the resulting plot (PNG file).
    xticks, yticks : list, optional
        Custom tick values for X and Y axes.
    xlabel : str, optional
        Custom label for X-axis.
    show_year_label : bool
        Whether to display the 'Year' label on the X-axis.
    year_label_pad : int
        Padding distance between axis and label.
    """

    # Build the path to the CSV file (life_expectancy_years.csv)
    csv_path = os.path.join(
        os.path.dirname(__file__),  # current directory
        'life_expectancy_years.csv',
    )

    # Use the local loader (ex01/load_csv.py). It will search sensible
    # candidate locations (including ../data) when given a basename.
    data = load(os.path.basename(csv_path))

    # If loader failed to load data, raise error
    if data is None:
        raise ValueError(f"Country '{country}' not found in dataset.")

    # ex00’s loader returns a DatasetView object that wraps a DataFrame.
    # It has a `.raw()` method to access the actual pandas DataFrame.
    # If the loader returns a plain DataFrame, we use it directly.
    if hasattr(data, 'raw'):
        df = data.raw()
    else:
        df = data

    # Check if the specified country exists in the dataset
    if country not in df['country'].values:
        raise ValueError(f"Country '{country}' not found in dataset.")

    # Filter rows for the chosen country and drop the 'country' column
    # Then transpose so that years become rows instead of columns
    country_data = df[df['country'] == country].drop(columns='country').T

    # Rename the single column to 'Life Expectancy'
    country_data.columns = ['Life Expectancy']

    # Reset the index (years) to become a proper column named 'Year'
    country_data.reset_index(inplace=True)

    # If the first column is not called 'Year', rename it
    if country_data.columns[0] != 'Year':
        country_data.rename(
            columns={country_data.columns[0]: 'Year'}, inplace=True
        )

    # Ensure that the 'Year' column is integer type
    country_data['Year'] = country_data['Year'].astype(int)

    # Ensure 'Life Expectancy' values are floats
    _col = 'Life Expectancy'
    country_data[_col] = country_data[_col].astype(float)

    # -----------------------------------------------------------
    # Plotting Part
    # -----------------------------------------------------------

    # Use seaborn’s default aesthetic theme
    sns.set_theme()

    # Create a line plot of life expectancy over years
    ax = sns.lineplot(
        data=country_data,
        x='Year',
        y='Life Expectancy',
        label='Life Expectancy',  # Label for legend
    )

    # Add a descriptive title to the plot
    ax.set_title(f"{country} Life Expectancy Projections")

    # Handle X-axis label visibility and positioning
    if xlabel:
        ax.set_xlabel(xlabel)
    elif show_year_label:
        # Show 'Year' label with custom padding (moves label down)
        ax.set_xlabel('Year', labelpad=year_label_pad)
    else:
        # Hide X-axis label completely
        # Seaborn will auto-set axis labels from the column names. If the
        ax.xaxis.label.set_visible(False)

    # Y-axis as 'Life Expectancy'
    ax.set_ylabel('Life Expectancy')

    # Configure tick marks (X-axis) ##
    # set xticks/yticks if provided, otherwise use a sensible locator
    if xticks:
        ax.set_xticks(xticks)
    else:
        # Automatically set ticks every 40 years if not provided
        ax.xaxis.set_major_locator(plticker.MultipleLocator(base=40))

    # Configure tick marks (Y-axis)
    if yticks:
        ax.set_yticks(yticks)

    # show legend (identifies the plotted series)
    ax.legend()

    # -----------------------------------------------------------
    # Output Section
    # -----------------------------------------------------------

    # If save_path is specified, save the plot as a PNG (headless mode)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()   # Close the figure to free memory!!
    else:
        plt.show()   # OR-> show the plot interactively (desktop mode)


# -----------------------------------------------------------
# MAIN | Command-line Interface (CLI) Section
# -----------------------------------------------------------
if __name__ == "__main__":
    import argparse

    def main() -> int:
        """CLI wrapper for `life_expectancy`.

        Parses command-line arguments and calls the plotting function.
        Exceptions are caught and reported; the function returns an
        appropriate exit code (0 on success, non-zero on error).
        """
        parser = argparse.ArgumentParser(
            description="Plot life expectancy for a country"
        )

        # Optional argument: specify country name (default = France)
        parser.add_argument("country", nargs="?", default="France")

        # Optional output filename flag
        parser.add_argument(
            "-o",
            "--out",
            help="Output filename for the plot (PNG)",
        )

        # Parse command-line arguments into 'args'
        args = parser.parse_args()
        out = args.out or f"{args.country.lower().replace(' ', '_')}_plot.png"

        # Define custom ticks for France example
        if args.country.lower() == "france":
            xticks = [1800, 1840, 1880, 1920, 1960, 2000, 2040, 2080]
            yticks = [30, 40, 50, 60, 70, 80, 90]
            xlabel = None
        else:
            xticks = None
            yticks = None
            xlabel = None

        try:
            life_expectancy(
                args.country,
                save_path=out,
                xticks=xticks,
                yticks=yticks,
                xlabel=xlabel,
            )
            return 0
        except Exception as e:
            print("Error:", e)
            return 1

    raise SystemExit(main())
