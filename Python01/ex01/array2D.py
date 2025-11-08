#!/usr/bin/env python3

"""Small helper to slice 2D lists using NumPy for the exercise.

This module provides a single helper, :func:`slice_me`, which accepts a
list-of-lists and returns the requested row slice as a list. The
implementation uses NumPy internally for convenience.
"""

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D list (family) from index ``start`` to ``end``.

    The function converts the input to a NumPy array, validates that
    it is two-dimensional and returns the requested row slice as a
    plain Python list-of-lists.
    """
    np_array = np.array(family)

    if np_array.ndim != 2:
        raise ValueError("family must be a 2D list (list of lists)")

    rows, cols = np_array.shape
    print(f"My shape is : ({rows}, {cols})")

    new_family = np_array[start:end]
    print(f"My new shape is : ({len(new_family)}, {cols})")

    return new_family.tolist()


def main() -> int:
    """Demo runner for the array2D slicing helper.

    The demo is guarded and catches exceptions so importing this module
    never triggers output or uncaught exceptions.
    """
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as exc:
        import sys

        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
