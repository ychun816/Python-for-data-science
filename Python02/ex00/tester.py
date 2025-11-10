#!/usr/bin/env python3

from load_csv import load

print(load("life_expectancy_years.csv"))

# OUTPUT
# $> python tester.py
# Loading dataset of dimensions (195, 302)
# country 1800 1801 1802 ... 2100
# Afghanistan 28.2 28.2 28.2 ... 76.8
# $>

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
