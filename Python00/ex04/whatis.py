#!/usr/bin/env python3

"""Check whether a single provided integer argument is odd or even.

All work is performed inside main() to avoid module-level globals and
side-effects on import.
"""

import sys


def main(argv: list[str] | None = None) -> None:
    argv = sys.argv if argv is None else argv

    if len(argv) == 1:
        return
    if len(argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    try:
        nb = int(argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    if nb % 2 != 0:
        print("I'm Odd.")
    else:
        print("I'm Even.")


if __name__ == "__main__":
    main()

# #OUTPUT
# $> python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# AssertionError: more than one argument is provided
# $>
