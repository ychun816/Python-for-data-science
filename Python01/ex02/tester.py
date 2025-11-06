#!usr/bin/env python3
"""Test runner for the image loader in ex02.

Moved demo code into a documented ``main`` function and added exception
handling so the script never raises uncaught exceptions at import time.
"""

import sys
from load_image import ft_load


def main(argv=None) -> int:

    """Run a simple load_image demo and print the returned value.

    Returns 0 on success, 1 on error.
    """
    argv = argv or sys.argv
    try:
        result = ft_load("happydoggie.jpg")
        print(result)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
