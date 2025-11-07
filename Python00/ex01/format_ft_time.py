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

### NOTES ###
