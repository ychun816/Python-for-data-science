#!/usr/bin/env python3
"""Simple CSV loader for the exercises using pandas.

This module exposes :func:`load` which reads a CSV file into a
``pandas.DataFrame``. The function validates the path and extension and
raises an informative exception on failure.
"""

import os
from typing import Optional  # For type hints (optional return type)
import pandas as pd  # Import pandas for working with tabular data


class DatasetView:
    """A tiny wrapper around a pandas DataFrame that prints a compact
    single-line preview (header + first row) with ellipses to match the
    exercise example while proxying attribute access to the underlying
    DataFrame.

    Use the :meth:`raw` method to retrieve the original pandas.DataFrame
    when you need to operate on or print the full dataset.
    """

    # Store the provided pandas DataFrame internally
    def __init__(self, df: pd.DataFrame):
        self._df = df

    # Delegate attribute access to the internal DataFrame
    # This allows DatasetView to behave like a DataFrame
    def __getattr__(self, name):
        return getattr(self._df, name)

    # Allow len(dataset_view) to return number of rows in the DataFrame
    def __len__(self):
        return len(self._df)

    def raw(self) -> pd.DataFrame:
        """Return the underlying pandas DataFrame.

        Use this when you need to access or print the full dataset (for
        example ``df = load(...).raw()`` or ``load(..., preview=False)``).
        """
        return self._df

    # Custom string representation for a concise preview
    def __repr__(self) -> str:
        df = self._df

        # header formatting: show a few leading and trailing columns
        # Extract column names and compute total number of columns
        cols = list(df.columns)
        n = len(cols)

        # lead-> Number of leading columns to show
        # trail-> Number of trailing columns to show
        lead = 4
        trail = 5

        # If few columns exist, show all; otherwise show truncated header
        if n <= lead + trail:
            header_cols = cols
        else:
            header_cols = cols[:lead] + ['...'] + cols[-trail:]

        # Attempt to get the first row for preview; handle errors safely
        # first row formatting
        try:
            first = df.iloc[0]
        except Exception:
            first = None

        # Helper function to format values for display
        def fmt_vals(vals):
            out = []
            for v in vals:
                if pd.isna(v):
                    out.append('NaN')  # Replace NaN with readable 'NaN'
                elif isinstance(v, float):
                    # show one decimal if fractional, else integer style
                    # Display floats neatly (no decimals if integer-like)
                    if abs(v - int(v)) < 1e-9:
                        out.append(str(int(v)))
                    else:
                        out.append(f"{v:.1f}")
                else:
                    out.append(str(v))  # Convert other data types to string
            return out

        # If the first row exists, select values for leading/trailing columns
        if first is not None:
            if n <= lead + trail:
                vals = fmt_vals(first.tolist())
            else:
                vals = (
                    fmt_vals(first.tolist()[:lead])
                    + ['...']
                    + fmt_vals(first.tolist()[-trail:])
                )
        else:
            vals = []

        # construct lines
        # Create header and row preview lines as space-separated strings
        header_line = ' '.join(str(c) for c in header_cols)
        row_line = ' '.join(vals)

        # Return a concise summary of dataset dimensions and a preview
        return (
            f"Loading dataset of dimensions {df.shape}\n"
            f"{header_line}\n{row_line}"
        )


def load(path: str, preview: bool = True) -> Optional[pd.DataFrame]:
    """Load a CSV file and return a pandas DataFrame.

    Parameters
    ----------
    path:
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame or DatasetView
        DataFrame with the CSV contents. If ``preview`` is True (default)
        the function returns a lightweight ``DatasetView`` whose printed
        representation is a compact preview matching the exercise example.
        If ``preview`` is False the raw ``pandas.DataFrame`` is returned.
    """
    # Resolve path: try given path, then the exercise directory, then ../data
    # Define possible file path candidates to search
    def _candidates(p: str):
        # 1. Try given path directly
        yield p
        # 2. Try a file in the same directory as this script
        yield os.path.join(os.path.dirname(__file__), p)
        # 3. Try a file in ../data relative to this script
        yield os.path.normpath(
            os.path.join(os.path.dirname(__file__), '..', 'data', p)
        )

    # Try to resolve the actual file path among the candidates
    resolved = None
    for cand in _candidates(path):
        try:
            if os.path.exists(cand):
                resolved = cand  # Found a valid path
                break
        except Exception:
            continue  # Ignore invalid paths and keep searching

    # If no file found, print an error and stop
    if resolved is None:
        print(f"File not found: {path}")
        return None

    # Validate file extension
    if not path.endswith(".csv"):
        print(f"Invalid file format: {path}. Expected a .csv file.")
        return None

    # Attempt to load CSV into a pandas DataFrame
    try:
        # Load CSV data into a DataFrame
        df = pd.read_csv(resolved)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

    # Handle empty file case
    if df.empty:  # check if file empty
        print(f"The file {path} is empty.")
        return None

    # Return raw DataFrame or the pretty-printing wrapper depending on
    # the preview flag requested by the caller.
    if preview:
        return DatasetView(df)
    return df


def main() -> int:
    """CLI-friendly entrypoint for a small loader demo.

    Attempts to load the shared `life_expectancy_years.csv` using the
    module's `load` function and prints a compact preview. Catches all
    exceptions and returns an exit code so nothing raises at global
    scope when the module is executed directly.
    """
    try:
        v = load("life_expectancy_years.csv")
        if v is None:
            print("Failed to load dataset")
            return 2
        print(v)
        return 0
    except Exception as e:
        print("Error while running load demo:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

# pandas documentation:
# https://pandas.pydata.org/docs/user_guide/index.html#user-guide

# Example usage (commented): get the raw pandas DataFrame or print the
# full table using the DatasetView convenience methods.
#
# v = load("life_expectancy_years.csv")
# df = v.raw()
# print(df.to_string())
#
# # or request the raw DataFrame directly from load:
# df2 = load("life_expectancy_years.csv", preview=False)
# print(df2.to_string())
#
# # If you enable the DatasetView.full() helper (it's commented in
# # load_csv.py), you can call: # v.full()
