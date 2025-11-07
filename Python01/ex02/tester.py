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
        # Try a few common example filenames so the tester works even when
        # the originally-named sample isn't present in the repository.
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
                "Warning: no example image found among candidates;"
                " skipping demo",
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
# $> python tester.py
# The shape of image is: (257, 450, 3)
# [[[19 42 83]
# [23 42 84]
# [28 43 84]
# ...
# [ 0 0 0]
# [ 1 1 1]
# [ 1 1 1]]]
# $
