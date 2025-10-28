#!/usr/bin/env python3
"""
CLI runner for ex03 projection plotting.

Usage examples (copy-paste to test):
  # show interactively (requires a display)
  python __main__.py 2019

  # save to a PNG in the repository root (headless-friendly)
  python __main__.py 2019 --save /workspaces/Python-for-data-science/ex03_2019_cli.png

  # short form
  python __main__.py 2019 -s ex03_2019.png

The --save / -s flag causes the script to save the current figure to the
given path instead of (or in addition to) attempting to open a GUI window.

Note: in headless containers there is no graphical DISPLAY, so calling
`plt.show()` will not open a window. Use --save when running inside a
container/remote environment.
"""

import sys
import argparse


def main(argv):
    parser = argparse.ArgumentParser(description="Plot GDP vs Life Expectancy for a year")
    parser.add_argument("year", help="Year to plot (e.g. 2010)")
    parser.add_argument("-s", "--save", dest="save", help="Path to save PNG instead of showing")
    args = parser.parse_args(argv[1:])

    # If user requested saving, switch to a non-interactive backend early.
    if args.save:
        try:
            import matplotlib
            matplotlib.use("Agg")
        except Exception:
            # If backend switch fails, we'll still attempt to save later.
            pass

    # Import exercise function after backend choice above (best-effort).
    try:
        from projection_life import gdp_life_expectancy
    except Exception as e:
        print(f"Import error: {e}")
        return 2

    try:
        gdp_life_expectancy(args.year)

        # If saving requested, capture and write the current figure
        if args.save:
            try:
                import matplotlib.pyplot as plt
                out = args.save
                fig = plt.gcf()
                fig.savefig(out, dpi=150, bbox_inches="tight")
                print(f"Saved plot to: {out}")
            except Exception as e:
                print(f"Failed to save plot: {e}")
                return 3

    except Exception as e:
        print(f"Exception: {e}")
        return 1

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)



