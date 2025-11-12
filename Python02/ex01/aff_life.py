#!/usr/bin/env python3

import os
import importlib.util
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as plticker
from typing import Optional


def _import_ex00_loader():
    """Dynamically import the `load` function from ex00/load_csv.py.

    Falls back to the local `load_csv` in this package if the ex00
    module cannot be found.
    """
    here = os.path.dirname(__file__)
    ex00_path = os.path.normpath(
        os.path.join(here, '..', 'ex00', 'load_csv.py')
    )
    if os.path.exists(ex00_path):
        spec = importlib.util.spec_from_file_location(
            'ex00_load_csv', ex00_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.load

    # fallback: try local load_csv.py
    try:
        from load_csv import load as _local_load

        return _local_load
    except Exception:
        msg = (
            'Could not import a suitable load function from ex00 '
            'or local file.'
        )
        raise ImportError(msg)


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
    """

    csv_path = os.path.join(
        os.path.dirname(__file__),
        'life_expectancy_years.csv',
    )
    # Use the basename so the ex00 loader can resolve the file from
    # the shared ../data directory when called from the exercises.
    loader = _import_ex00_loader()
    data = loader(os.path.basename(csv_path))

    if data is None:
        raise ValueError(f"Country '{country}' not found in dataset.")

    # `ex00`'s loader returns a DatasetView (which proxies attributes but
    # doesn't implement __getitem__). Extract the raw DataFrame when
    # present so we can index by column name regardless of loader.
    if hasattr(data, 'raw'):
        df = data.raw()
    else:
        df = data

    if country not in df['country'].values:
        raise ValueError(f"Country '{country}' not found in dataset.")

    country_data = df[df['country'] == country].drop(columns='country').T
    country_data.columns = ['Life Expectancy']
    # Ensure the index becomes a 'Year' column after reset_index.
    # Some loaders may not name the index, so normalize the column name
    # produced by reset_index to 'Year'.
    country_data.reset_index(inplace=True)
    if country_data.columns[0] != 'Year':
        country_data.rename(
            columns={country_data.columns[0]: 'Year'}, inplace=True
        )

    country_data['Year'] = country_data['Year'].astype(int)
    _col = 'Life Expectancy'
    country_data[_col] = country_data[_col].astype(float)

    sns.set_theme()
    # label the plotted line so a legend can be shown
    ax = sns.lineplot(
        data=country_data,
        x='Year',
        y='Life Expectancy',
        label='Life Expectancy',
    )
    ax.set_title(f"{country} Life Expectancy Projections")
    # axis labels required by the exercise (allow overrides)
    # If an explicit xlabel is provided, use it. Otherwise, optionally
    # show the default 'Year' label and move it using labelpad so it
    # sits lower than usual (the user asked to "move x-axis label").
    if xlabel:
        ax.set_xlabel(xlabel)
    elif show_year_label:
        ax.set_xlabel('Year', labelpad=year_label_pad)
    else:
        # Seaborn will auto-set axis labels from the column names. If the
        # user requested no year label we must explicitly hide it.
        ax.xaxis.label.set_visible(False)

    ax.set_ylabel('Life Expectancy')

    # set xticks/yticks if provided, otherwise use a sensible locator
    if xticks:
        ax.set_xticks(xticks)
    else:
        ax.xaxis.set_major_locator(plticker.MultipleLocator(base=40))

    if yticks:
        ax.set_yticks(yticks)
    # show legend (identifies the plotted series)
    ax.legend()
    # If a save path is provided, save the figure to a file. This makes
    # the function work in headless / CI environments where ``plt.show()``
    # may not display anything. Otherwise show the interactive window.
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
    else:
        plt.show()


if __name__ == "__main__":
    import argparse

    def main() -> int:
        """CLI wrapper for `life_expectancy`.

        Parses command-line arguments and calls the plotting function.
        Exceptions are caught and reported; the function returns an
        appropriate exit code (0 on success, non-zero on error).
        """
        parser = argparse.ArgumentParser(
            description='Plot life expectancy for a country'
        )
        parser.add_argument('country', nargs='?', default='France')
        parser.add_argument(
            '-o', '--out', help='Output filename for the plot (PNG)'
        )
        args = parser.parse_args()

        out = args.out or f"{args.country.lower().replace(' ', '_')}_plot.png"

        # Use the requested ticks for the France example.
        if args.country.lower() == 'france':
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
