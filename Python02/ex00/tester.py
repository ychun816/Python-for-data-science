#! usr/bin/env python3


from load_csv import load
print(load("life_expectancy_years.csv"))
# print(load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))
# print(load("population_total.csv"))

# OUPTUT
# $> python tester.py
# Loading dataset of dimensions (195, 302)
# country 1800 1801 1802 1803 ... 2096 2097 2098 2099 2100
# Afghanistan 28.2 28.2 28.2 28.2 ... 76.2 76.4 76.5 76.6 76.8
# ...
# $>