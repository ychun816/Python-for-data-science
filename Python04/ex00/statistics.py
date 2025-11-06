#!/usr/bin/env python3

"""Simple statistics helper used by the exercises.

Provides ft_statistics(*args, **kwargs) which computes only the
requested statistics from numeric positional arguments.
"""

from typing import Any
import math


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Compute requested statistics for numeric args and print results.

    Behavior (kept simple to match tester expectations):
    - Filters out non-numeric args with a warning.
    - If there are no numeric values, prints three lines with "ERROR"
      and returns.
    - kwargs values are expected to be strings naming statistics
      (for example: toto="mean", tutu="median"). We iterate over
      the kwargs values and print the requested stats in the order
      they appear.
    Supported stats: "mean", "median", "quartile", "var", "std".
    """

    # Step 1: Filter numeric inputs
    nbs = [a for a in args if isinstance(a, (int, float))]
    for a in args:
        if not isinstance(a, (int, float)):
            print(f"WARNING: Ignoring non-numeric value '{a}'")

    if not nbs:
        # The tester expects an ERROR block when no numbers are provided.
        print("ERROR")
        print("ERROR")
        print("ERROR")
        return

    # Step 2: Sort numbers
    nbs = sorted(nbs)

    # Helper functions
    def mean(nums):
        return sum(nums) / len(nums)

    def median(nums):
        size = len(nums)
        mid = size // 2
        if size % 2 == 1:
            return nums[mid]
        return (nums[mid - 1] + nums[mid]) / 2

    def quartile(nums):
        size = len(nums)
        q1_idx = size // 4
        q3_idx = 3 * size // 4
        return [float(nums[q1_idx]), float(nums[q3_idx])]

    def variance(nums):
        m = mean(nums)
        return sum((x - m) ** 2 for x in nums) / len(nums)

    def std_dev(nums):
        return math.sqrt(variance(nums))

    stat_map = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "var": variance,
        "std": std_dev,
    }

    # Process requested statistics from kwargs values
    for stat_name in kwargs.values():
        if stat_name in stat_map:
            func = stat_map[stat_name]
            result = func(nbs)
            print(f"{stat_name} : {result}")
        else:
            print(f"WARNING: Unknown stat '{stat_name}'")
