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

    Raises TypeError if inputs are not numeric.
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


def main() -> int:
    """Simple CLI demo for the give_bmi utilities.

    This function is intentionally small and only used when the module is
    executed as a script. It catches all exceptions and returns a numeric
    exit code so callers (CI/test harness) never receive an uncaught
    exception.
    """
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as exc:
        import sys

        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())


# In Python, when you write code directly in the file (outside any function or class), 
# it will run immediately when the file is executed or imported.
# -> global code always runs, even if you just import the file
# -> when someone imports your file (for testing or reuse),
# you don’t want your code to execute automatically — it should only run when you explicitly tell it to.
# def main():
#     # your program here
# if __name__ == "__main__":
#     main()


# def main():
#     # simple demo when run as a script
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))

# When to define main:
# - Module with a guarded demo main() (convenience)
# - Safe to import; demo runs only when you call python give_bmi.py
# - Module as CLI (use when you want command-line behavior)

# | Name       | English Explanation                                      | 中文解釋                         |
# | ---------- | -------------------------------------------------------- | ---------------------------- |
# | `__name__` | Identifier of the module; `"__main__"` when run directly | 模組名稱；當直接執行檔案時等於 `"__main__"` |
# | `__main__` | The name Python assigns to the top-level script          | Python 對主程式檔案給的名稱            |
# | `__doc__`  | String containing the function’s documentation           | 函式或模組的文件字串（說明文字）             |

