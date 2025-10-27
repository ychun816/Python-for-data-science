#! usr/bin/env python3

import os #path check
import pandas as pd #visualize data

#  -> Dataset: (You have to adapt the type of return according to your library)
def load(path: str) -> pd.DataFrame:
    """
    load takes a csv file path and returns a data frame.

    Parameters:
    path (str): path of the csv file.

    Return Value:
    dataframe (Pandas DataFrame): a dataframe containing the csv's content.
    """

    #error check
    #-cant find path
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
        # print(f"File not found: {path}")
        # return None
    #-bad extension
    if not path.endswith('.csv'):
        raise ValueError(f"Invalid file format: {path}. Expected a .csv file.")
        # print(f"Invalid file format: {path}. Expected a .csv file.")
        # return None

    try:
        # Load csv data into a dataframe
        df = pd.read_csv(path)
        if df.empty: #chec if file empty
            raise ValueError(f"The file {path} is empty.")

        print(f"Dataset dimensions: {df.shape}")
        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")  # just prints error, but returns None
        raise #re-throws the same exception upward  #try -> except -> (print) -> raise -> back to main() or tester.py
        # return None

