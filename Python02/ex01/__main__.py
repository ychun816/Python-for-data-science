#!/usr/bin/env python3

import sys

from aff_life import life_expectancy


def main(argv):
    if len(argv) != 2:
        print("Usage: __main__.py '<country_name>'")
        return 1

    try:
        life_expectancy(argv[1])
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
