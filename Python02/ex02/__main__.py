#!/usr/bin/env python3

import sys
from aff_pop import population_total


def main(argv):
    try:
        assert len(argv) == 3, "Usage: __main__.py <country> <compare_country>"
        population_total(argv[1], argv[2])

    except Exception as e:
        print(f"An error occurred: {e}")
        return 1  # sys.exit(1)
    return 0  # sys.exit(0)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
