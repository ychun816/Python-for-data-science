#!/usr/bin/env python3
"""Simple CSV loader for the exercises using pandas.

This module exposes :func:`load` which reads a CSV file into a
``pandas.DataFrame``. The function validates the path and extension and
raises an informative exception on failure.
"""

import os
from typing import Optional
import pandas as pd


class DatasetView:
    """A tiny wrapper around a pandas DataFrame that prints a compact
    single-line preview (header + first row) with ellipses to match the
    exercise example while proxying attribute access to the underlying
    DataFrame.

    Use the :meth:`raw` method to retrieve the original pandas.DataFrame
    when you need to operate on or print the full dataset.
    """

    def __init__(self, df: pd.DataFrame):
        self._df = df

    def __getattr__(self, name):
        return getattr(self._df, name)

    def __len__(self):
        return len(self._df)

    def raw(self) -> pd.DataFrame:
        """Return the underlying pandas DataFrame.

        Use this when you need to access or print the full dataset (for
        example ``df = load(...).raw()`` or ``load(..., preview=False)``).
        """
        return self._df

    def __repr__(self) -> str:
        df = self._df
        # header formatting: show a few leading and trailing columns
        cols = list(df.columns)
        n = len(cols)
        lead = 4
        trail = 5
        if n <= lead + trail:
            header_cols = cols
        else:
            header_cols = cols[:lead] + ['...'] + cols[-trail:]

        # first row formatting
        try:
            first = df.iloc[0]
        except Exception:
            first = None

        def fmt_vals(vals):
            out = []
            for v in vals:
                if pd.isna(v):
                    out.append('NaN')
                elif isinstance(v, float):
                    # show one decimal if fractional, else integer style
                    if abs(v - int(v)) < 1e-9:
                        out.append(str(int(v)))
                    else:
                        out.append(f"{v:.1f}")
                else:
                    out.append(str(v))
            return out

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
        header_line = ' '.join(str(c) for c in header_cols)
        row_line = ' '.join(vals)

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
    def _candidates(p: str):
        # If absolute or contains a directory, try it as-is first
        yield p
        # Try next to this module (ex00 folder)
        yield os.path.join(os.path.dirname(__file__), p)
        # Try Python02/data relative to this module
        yield os.path.normpath(
            os.path.join(os.path.dirname(__file__), '..', 'data', p)
        )

    resolved = None
    for cand in _candidates(path):
        try:
            if os.path.exists(cand):
                resolved = cand
                break
        except Exception:
            continue

    if resolved is None:
        print(f"File not found: {path}")
        return None

    if not path.endswith(".csv"):
        print(f"Invalid file format: {path}. Expected a .csv file.")
        return None

    try:
        # Load CSV data into a DataFrame
        df = pd.read_csv(resolved)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

    if df.empty:  # check if file empty
        print(f"The file {path} is empty.")
        return None

    # Return raw DataFrame or the pretty-printing wrapper depending on
    # the preview flag requested by the caller.
    if preview:
        return DatasetView(df)
    return df
