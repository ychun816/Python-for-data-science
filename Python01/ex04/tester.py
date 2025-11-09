#!/usr/bin/env python3
"""Test runner for the ex04 image loader.

This tester includes a documented main() and a guarded entry so importing
it does not produce side effects or uncaught exceptions.
"""

import sys
from load_image import ft_load


def main(argv=None) -> int:
    """Run a short demo of ft_load and return 0 on success, 1 on error."""
    argv = argv or sys.argv
    try:
        candidates = [
            "happydoggie.jpg",
            "animal.jpeg",
            "landscape.jpg",
        ]
        result = None
        for name in candidates:
            result = ft_load(name)
            if result is not None:
                break

        if result is None:
            print(
                "Warning: no example image found among candidates; "
                "skipping demo",
                file=sys.stderr,
            )
        else:
            print(result)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

# OUTPUT
# $> python rotate.py
# The shape of image is: (400, 400, 1) or (400, 400)
# [[[167]
# [180]
# [194]
# ...
# [102]
# [104]
# [103]]]
# New shape after Transpose: (400, 400)
# [[167 180 194 ... 64 50 72]
# ...
# [115 116 119 ... 102 104 103]]
# $>