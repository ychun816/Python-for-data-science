#!/usr/bin/env python3

from load_csv import load


def main() -> None:
    """Simple tester for the CSV loader used during development."""
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
