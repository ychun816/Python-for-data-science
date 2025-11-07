#!/usr/bin/env python3

"""Tester for NULL_not_found — placed in main() to avoid globals.
"""

from NULL_not_found import NULL_not_found


def main() -> None:
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ""
    Fake = False

    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)

    print(NULL_not_found("Brian"))


if __name__ == "__main__":
    main()

# OUTPUT
# $>python tester.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
# $>
# $>python NULL_not_found.py | cat -e
# $>
