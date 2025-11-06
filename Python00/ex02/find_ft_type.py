#!/usr/bin/env python3

"""Helper: print a readable type description for a value.

The function returns 42 to match the original exercise's expected
return value.
"""


def all_thing_is_obj(value: any) -> int:
    """Print a short description of the runtime type of value.

    Returns:
        int: always 42 (exercise requirement)
    """
    if isinstance(value, list):
        print("List:", type(value))
    elif isinstance(value, tuple):
        print("Tuple:", type(value))
    elif isinstance(value, set):
        print("Set:", type(value))
    elif isinstance(value, dict):
        print("Dict:", type(value))
    elif isinstance(value, str):
        print(f"{value} is a string: {type(value)}")
    else:
        print("this type not found")
    return 42
