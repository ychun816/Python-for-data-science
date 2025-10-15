#!/usr/bin/env python3
"""BMI utilities.

This module provides small helper functions to compute Body Mass Index (BMI)
values from lists of heights and weights and to compare BMI values to a
threshold limit.

The functions are import-safe and any demo code is guarded by
``if __name__ == "__main__":``.
"""


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Compute BMI values for paired height and weight lists.

    Args:
        height: Sequence of heights in meters.
        weight: Sequence of weights in kilograms. Must be the same length as
            ``height``.

    Returns:
        A list of BMI values (weight / height**2) in the same order as inputs.

    Raises:
        ValueError: If the lengths of the input lists differ.
        TypeError: If any height or weight value is not an int or a float.
    """

    # handle error
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be the same length.")

    # check value -> need to be int or float
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("All height and weight values must be int or float.")

    #calculate bmi
    bmi_list = [w / (h ** 2) for h, w in zip(height, weight)]
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]: 
    #handle error -> not int or float
    # “Are all values in the list bmi numbers?”
    # “If NOT all values are numeric → raise an error.”
    if not all(isinstance(b_value, (int, float)) for b_value in bmi):
        raise TypeError("BMI values must be int or float.")
    # handle error -> limit not int or float
    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be a number.")

    # compare bmi & limit
    result = [b_value > limit for b_value in bmi]
    return result




# def main():
#     # simple demo when run as a script
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))


# if __name__ == "__main__":
#     main()

### NOTES ####
# height: list[int | float], weight: list[int | float] -> list[int | float]
# height list (could be more than 1 element) -> should be int or float 
# -> list[int | float ] -> return value should be int or float 

# for ... in ... → looping through items in a list or iterable
# zip() → combines lists element by element
# Example: zip([1,2,3], ['a','b','c']) -> [(1,'a'), (2,'b'), (3,'c')]
# [
#   weight[0] / (height[0] ** 2),
#   weight[1] / (height[1] ** 2),
#   ...
# ]

# isinstance(x, (int, float))
# -> checks if variable x is either an int or a float. Returns True or False.

# not
# reverses the result (turns True → False, False → True).

# all()
# -> a built-in function that checks if all elements inside are True.
# all([True, True, True])   → True
# all([True, False, True])  → False


# when to define main :  
# - Module with a guarded demo main() (convenience)
# - Safe to import; demo runs only when you call python give_bmi.py
# - Module as CLI (use when you want command-line behavior)

##############