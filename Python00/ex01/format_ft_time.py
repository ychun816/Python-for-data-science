#!/usr/bin/env python3

"""Format and print epoch time and a human-readable date.

Placed inside main() to avoid module-level globals/side-effects.
"""

import time
import datetime


def main() -> None:
    # Get current time in seconds since epoch
    epoch = time.time()

    # Format numbers
    format_normal = f"{epoch:,.4f}"
    format_sci = f"{epoch:.2e}"

    # Format date
    now = datetime.datetime.now()
    format_date = now.strftime("%b %d %Y")

    # Print results
    print(
        f"Seconds since January 1, 1970: {format_normal} or {format_sci}"
        " in scientific notation"
    )
    print(format_date)


if __name__ == "__main__":
    main()

# OUTPUT
# $> python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09
# in scientific notation$
# Oct 21 2022$
# $>

# NOTES
# Libraries:
# - time: https://docs.python.org/3/library/time.html
# - datetime: https://docs.python.org/3/library/datetime.html

# - time.time() returns the current time in seconds since the epoch
#   (January 1, 1970)
# - f-strings can be used to format numbers with commas and decimals
# - datetime module is used to get the current date and format it
#   as a string

# About __name__
# Every Python module has a built-in variable called __name__.
# When Python runs a file directly (for example: python myfile.py),
# it sets __name__ = "__main__" for that execution.
# When the same file is imported, Python sets __name__ to the
# module's filename (for example: "format_ft_time").
