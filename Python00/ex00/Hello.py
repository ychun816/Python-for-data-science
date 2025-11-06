#!/usr/bin/env python3

"""Simple demo of Python container types.

This script places example code in main() to avoid module-level globals
and side effects at import time.
"""


def main() -> None:
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    # Modify values locally inside main (no module-level globals)
    ft_list[1] = "World!"
    ft_tuple = (ft_tuple[0], "France!")
    ft_set = {"Hello", "Paris!"}
    ft_dict["Hello"] = "42Paris!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()
