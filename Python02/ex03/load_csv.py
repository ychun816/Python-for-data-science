#!/usr/bin/env python3
"""Simple CSV loader for the exercises using pandas.

This module exposes :func:`load` which reads a CSV file into a
``pandas.DataFrame``. The function validates the path and extension and
raises an informative exception on failure.
"""

import os
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file and return a pandas DataFrame.

    Parameters
    ----------
    path:
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        DataFrame with the CSV contents.
    """

    # Error checks
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    if not path.endswith(".csv"):
        raise ValueError(f"Invalid file format: {path}. Expected a .csv file.")

    try:
        # Load CSV data into a DataFrame
        df = pd.read_csv(path)
        if df.empty:  # check if file empty
            raise ValueError(f"The file {path} is empty.")

        print(f"Dataset dimensions: {df.shape}")
        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")
        raise
