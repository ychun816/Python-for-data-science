#! usr/bin/env python3

import sys
import os                     # for file path handling
import numpy as np            # for array manipulation
import pandas as pd           # for DataFrame handling
import seaborn as sns         # for plotting


from matplotlib import pyplot as plt
from matplotlib import ticker as plticker

from aff_life import life_expectancy
from load_csv import load

def main(argv):
    try:
        assert len(sys.argv) == 2, "Usage: __main__.py '<country_name>'"
        life_expectancy(sys.argv[1])
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1 # sys.exit(1)
    return 0 # sys.exit(0)

if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # sys.exit(1)