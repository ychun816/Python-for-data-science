#! usr/bin/env python3

# 1. Function: ft_statistics(*args, **kwargs)
# - *args: unknown number of numerical inputs
# - **kwargs: unknown number of “requests” for statistics (like mean, median, quartile, std, var)
# 2. Must calculate only the requested statistics.
# 3. Must handle errors, including:
# - No numbers in args
# - Invalid kwargs names
# 4. Must not use external libraries except standard ones.

# from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None
   """Function to filter list numbers and extract values"""
    # Step 1: Check if args exist
   if not args:
        print("----- ERROR")
        print("ERROR ERROR")
        return

    # Step 2: Filter only numeric values
    nbs = []
    for arg in args:
        if isinstance(arg, (int, float)):
            nbs.append(arg)
        else:
            print(f"WARNING: Ignoring non-numeric value '{arg}'")
    
    if not nbs:
        print("----- ERROR")
        print("ERROR ERROR")
        return

    # Step 3: Sort numbers manually (bubble sort)
    nbs_size = len(nbs)
    for i in range(nbs_size):
        for j in range(0, nbs_size-i-1):
            if nbs[j] > nbs[j+1]:
                nbs[j], nbs[j+1] = nbs[j+1], nbs[j]

    # Step 4: Helper functions implemented manually
    #mean
    def mean(nb):
        """get mean"""
        total = 0
        for x in nbs:
            total += x
        return total / len(nbs)

    #median
    def median(nb):
        """get median (middle value after sorting)"""
        size = len(nbs)
        mid = size // 2
        if size % 2 == 0:
            return (nbs[mid-1] + nbs[mid]) / 2

    #quartile
    def quartile(nb):
        """get quartile (Q1 = 25%, Q3 = 75%, sort + pick indices)"""
        size = len(nbs)
        q1_idx = size // 4
        q3_indx = 3 * size // 4
        return [nbs[q1_idx], nbs[q3_idx]]

    #variance
    def variance(nb):
        """get variance, sum((x - mean)^2)/n """
        m = mean(nbs)
        return sum((x - m)**2 for x in nums) / len(nums)

    #std_dev
    def std_dev(nb):
        """get std_dev, sqrt(variance)"""
        return math.sqrt(variance(nbs))

    # Step 5: Map string keys to functions
    stat_map = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "var": variance,
        "std": std_dev
    }

    # Step 6: Process kwargs
    for key in kwargs:
        stat_name = kwargs[key]

        if stat_name in stat_map:
            func = stat_map[stat_name]
            result = func(nbs)
            print(f"{stat_name} : {result}")
        else:
            print(f"WARNING: Unknown stat '{stat_name}'")




### NOTES ###

# | Statistic | Formula / Method                         |
# | --------- | ---------------------------------------- |
# | Mean      | sum(numbers) / len(numbers)              |
# | Median    | middle value after sorting               |
# | Quartile  | Q1 = 25%, Q3 = 75% (sort + pick indices) |
# | Variance  | sum((x - mean)^2)/n                      |
# | Std Dev   | sqrt(variance)                           |


