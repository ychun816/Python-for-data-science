#!usr/bin/env python3
"""Test runner for the array2D slicing utilities.

Moved top-level demo code into a documented ``main`` function and added a
guarded entry which catches exceptions so tests never raise uncaught
exceptions at import time.
"""

import sys
from array2D import slice_me


def main(argv=None) -> int:
    """Run the array2D demo and print slices.

    Returns 0 on success, 1 on any error.
    """
    argv = argv or sys.argv
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

# OUTPUT
# $> python test_array2D.py
# My shape is : (4, 2)
# My new shape is : (2, 2)
# [[1.8, 78.4], [2.15, 102.7]]
# My shape is : (4, 2)
# My new shape is : (1, 2)
# [[2.15, 102.7]]
# $
