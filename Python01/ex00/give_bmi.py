#!/usr/bin/env python3
"""BMI utilities.

Helpers to compute Body Mass Index (BMI) from lists of heights and
weights. Also includes a small helper to compare BMI values against a
numeric threshold.

Functions are import-safe; guard any demo code using::

    if __name__ == "__main__":
        ...
"""


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Compute BMI values for paired height and weight lists.

    Args:
        height: Sequence of heights in meters.
        weight: Sequence of weights in kilograms.
            Must be the same length as ``height``.

    Returns:
        A list of BMI values (weight / height**2).
        The result order matches the input order.

    Raises:
        ValueError: If the lengths of the input lists differ.
        TypeError: If any height or weight value is not an int or float.
    """

    # handle error
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be the same length.")

    # check value -> need to be int or float
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("All height and weight values must be numbers.")

    # calculate bmi
    bmi_list = [w / (h ** 2) for h, w in zip(height, weight)]
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans indicating which BMI values exceed limit.

    Raises TypeError if inputs are not numeric.. krkr
    """
    # handle error -> not int or float
    # Are all values in the list bmi numbers?
    # If not all values are numeric -> raise an error.
    if not all(isinstance(b_value, (int, float)) for b_value in bmi):
        raise TypeError("BMI values must be int or float.")
    # handle error -> limit not int or float
    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be a number.")

    # compare bmi & limit
    result = [b_value > limit for b_value in bmi]

    # Keep a small commented demo below; the function itself returns
    # the boolean list showing which BMI values exceed the limit.
    return result

def main(argv=None) -> int:
    """Run a short demo of ``give_bmi`` and ``apply_limit``.

    Returns 0 on success or 1 on error (so callers can use ``sys.exit``).
    """
    argv = argv or sys.argv
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

# NOTES ########
# - Code at module level runs when the file is executed or imported.
# - Keep demo code inside a guarded main() so importing is safe.

# - zip(height, weight): pair corresponding items from two sequences
#   (stops when the shortest is exhausted).

# - all(isinstance(x, (int, float)) for x in seq): True if every
#   element of seq is numeric (short-circuits on first False).

# - [b > limit for b in bmi]: list comprehension producing booleans
#   indicating which BMI values exceed the given limit.

# sys.exit(main()) runs your program's main() function 
# and asks Python to terminate process using main()'s return value as the process exit code.
############################

# TESTER.PY ########

# #!/usr/bin/env python3
# """Test runner for the ``give_bmi`` utilities.

# This file contains a documented ``main`` function and an
# ``if __name__ == "__main__"`` guard so the module is import-safe.
# """

# import sys
# from give_bmi import give_bmi, apply_limit


# def main(argv=None) -> int:
#     """Run a short demo of ``give_bmi`` and ``apply_limit``.

#     Returns 0 on success or 1 on error (so callers can use ``sys.exit``).
#     """
#     argv = argv or sys.argv
#     try:
#         height = [2.71, 1.15]
#         weight = [165.3, 38.4]
#         bmi = give_bmi(height, weight)
#         print(bmi, type(bmi))
#         print(apply_limit(bmi, 26))
#     except Exception as exc:
#         print(f"Error: {exc}", file=sys.stderr)
#         return 1
#     return 0


# if __name__ == "__main__":
#     sys.exit(main())

# OUTPUT
# $> python tester.py
# [22.507863455018317, 29.0359168241966] <class 'list'>
# [False, True]
# $>

############################
