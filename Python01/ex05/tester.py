#!/usr/bin/env python3
"""Test runner for the pimp_image utilities.

Moved top-level calls into a documented ``main`` function and added
exception handling so the module is import-safe and respects the norm.
"""

import sys
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main(argv=None) -> int:
    """Load the example image and run a few pimp functions.

    Returns 0 on success, 1 on error.
    """
    argv = argv or sys.argv
    try:
        array = ft_load("landscape.jpg")
        if isinstance(array, str) and array.startswith("Error:"):
            # preserve existing behaviour where ft_load returns error strings
            print(array, file=sys.stderr)
            return 1

        # Call transformations (they return arrays but keep side effects local)
        _ = ft_invert(array)
        _ = ft_red(array)
        _ = ft_green(array)
        _ = ft_blue(array)
        _ = ft_grey(array)

        # print documentation example
        print(ft_invert.__doc__)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
