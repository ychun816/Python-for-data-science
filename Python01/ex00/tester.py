#!/usr/bin/env python3
"""Test runner for the ``give_bmi`` utilities.

This file contains a documented ``main`` function and an
``if __name__ == "__main__"`` guard so the module is import-safe.
"""

import sys
from give_bmi import give_bmi, apply_limit


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

# OUTPUT
# $> python tester.py
# [22.507863455018317, 29.0359168241966] <class 'list'>
# [False, True]
# $>