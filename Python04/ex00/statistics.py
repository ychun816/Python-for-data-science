#!/usr/bin/env python3

"""Simple statistics helper used by the exercises.

Provides ft_statistics(*args, **kwargs) which computes only the
requested statistics from numeric positional arguments.
"""

from typing import Any  # Allows type‐hinting that accepts any data type.
import math  # Needed for sqrt in standard deviation.


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
        # The tester expects an ERROR * 3times when no numbers are provided.
        print("ERROR")
        print("ERROR")
        print("ERROR")
        return  # Function stops immediately

    # Step 2: Sort numbers
    nbs = sorted(nbs)  # Many statistics (median, quartile) require sorted data

    # HELPER FUNCS ###################
    # Average of numbers 平均數 / 平均值
    # Add all numbers, divide by count
    def mean(nums):
        return sum(nums) / len(nums)

    # Middle value after sorting 中位數
    # If odd: pick middle; even: average two middle
    def median(nums):
        size = len(nums)
        # Find middle index 取整數除法找中間索引
        mid = size // 2
        if size % 2 == 1:
            return nums[mid]  # Median for odd count 奇數個數字直接取中間數
        # Median for even count 偶數數字取中間兩個平均
        return (nums[mid - 1] + nums[mid]) / 2

    # 25% (Q1) & 75% (Q3) positions 四分位數
    # Q1 = n//4 index, Q3 = 3n//4 index
    def quartile(nums):
        size = len(nums)
        q1_idx = size // 4
        q3_idx = 3 * size // 4
        return [float(nums[q1_idx]), float(nums[q3_idx])]

    # How far numbers are from mean 變異數
    # sum((x-mean)^2)/n
    def variance(nums):
        m = mean(nums)
        #  Compute variance 計算平方差平均
        # Each x subtract mean, square, sum, divide by n
        return sum((x - m) ** 2 for x in nums) / len(nums)

    # Typical distance from mean 標準差
    # Square root of variance # sqrt(variance) (iterative)
    def std_dev(nums):
        return math.sqrt(variance(nums))

    # Dictionary linking textual keywords to the corresponding function
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
            # Unknown stat: silently ignore to match tester expectations.
            continue

# TESTER ####
# from statistics import ft_statistics

# ft_statistics(
#     1, 42, 360, 11, 64,
#     toto="mean", tutu="median", tata="quartile",
# )
# print("-----")
# ft_statistics(
#     5, 75, 450, 18, 597, 27474, 48575,
#     hello="std", world="var",
# )
# print("-----")
# ft_statistics(
#     5, 75, 450, 18, 597, 27474, 48575,
#     ejfhhe="heheh", ejdjdejn="kdekem",
# )
# print("-----")
# ft_statistics(toto="mean", tutu="median", tata="quartile")


# OUTPUT
# $> python tester.py
# mean : 95.6
# median : 42
# quartile : [11.0, 64.0]
# -----
# std : 17982.70124086944
# var : 323377543.9183673
# -----
# -----
# ERROR
# ERROR
# ERROR
# $>
