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

# NOTES ########
# np.array(family): convert list-of-lists to a NumPy array.
# np_array.shape: (rows, cols) tuple with array dimensions.
# new_family = np_array[start:end]: slice rows start..end-1.
# new_family.tolist(): convert NumPy array back to Python lists.

###################################

# TESTER.PY ########

# from array2D import slice_me


# def main(argv=None) -> int:
#     """Run the array2D demo and print slices.

#     Returns 0 on success, 1 on any error.
#     """
#     argv = argv or sys.argv
#     try:
#         family = [[1.80, 78.4],
#                   [2.15, 102.7],
#                   [2.10, 98.5],
#                   [1.88, 75.2]]
#         print(slice_me(family, 0, 2))
#         print(slice_me(family, 1, -2))
#     except Exception as exc:
#         print(f"Error: {exc}", file=sys.stderr)
#         return 1
#     return 0


# if __name__ == "__main__":
#     sys.exit(main())

# OUTPUT
# $> python test_array2D.py
# My shape is : (4, 2)
# My new shape is : (2, 2)
# [[1.8, 78.4], [2.15, 102.7]]
# My shape is : (4, 2)
# My new shape is : (1, 2)
# [[2.15, 102.7]]
# $
#############################
