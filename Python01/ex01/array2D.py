#!usr/bin/env python3

#Method 1: basics without numPY
# def slice_me(family: list, start: int, end: int) -> list: 
#     #check if format right (list of lists, 2D)
#     if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
#         raise ValueError("family must be a 2D list (list of lists)")
#     #check if all rows have same len
#     row_length = len(family[0])
#     if not all(len(row) == row_length for row in family):
#         raise ValueError("All rows in family must have the same length")

#     #print og shape
#     print(f"My shape is : ({len(family)}, {row_length})")

#     #slicing
#     new_family = family[start:end]
#     #print new shape
#     print(f"My new shape is : ({len(new_family)}, {row_length})")

#     return new_family


# Method 2 : with numbPY
import numpy as np
def slice_me(family: list, start: int, end: int) -> list: 
    #convert to numpy array
    np_array = np.array(family)

    #check if 2D
    if np_array.ndim != 2:
        raise ValueError("family must be a 2D list (list of lists)")

    rows, cols = np_array.shape[0], np_array.shape[1]  # only if array is 2D

    #print og shape
    print(f"My shape is : ({rows}, {cols})")

    #slicing
    new_family = np_array[start:end]

    #print new shape
    print(f"My new shape is : ({rows}, {cols})")
    
    # convert back to list if needed
    new_family_list_form = new_family.tolist()
    return new_family_list_form  


### NOTES ### 

# Shape = The blueprint of your data.
# It shows how many dimensions and how big each dimension is.
# “Size” = total number of elements → e.g. (4, 2) → size = 8
# “Shape” = structure (rows, cols, depth)

# KEY CONCEPTS:
# - Positive indexes count from front.
# - Negative indexes count from back.
# - Slice stops before the end index.
# - If start > end (and no negative step), result = [].


# list[1:3]
# | index | value (height, weight) |
# | :---: | ---------------------- |
# |   0   | [1.80, 78.4]           |
# |   1   | [2.15, 102.7]          |
# |   2   | [2.10, 98.5]           |
# |   3   | [1.88, 75.2]           |

# family = [
#   [1.80, 78.4],   # index 0
#   [2.15, 102.7],  # index 1
#   [2.10, 98.5],   # index 2
#   [1.88, 75.2]    # index 3
# ]

# | index | -index equivalent |
# | ----- | ----------------- |
# | 0     | -4                |
# | 1     | -3                |
# | 2     | -2                |
# | 3     | -1                |


# family[-1] → last element (index 3)
# family[-2] → second-to-last element (index 2)

# slice [1:-2]
# -> Start from index 1, go until index -2, but stop before it.
# index 1  ✅
# index 2  ❌ (stop here)
# index 3  ❌

# Index:     0          1          2          3
#            ----------------------------------------
# family = [ [1.80,78.4], [2.15,102.7], [2.10,98.5], [1.88,75.2] ]
# Slice:              [===========)
#                     ↑         ↑
#                start=1     stop=-2 (=index 2)



# | Feature        | Plain Python             | NumPy                           |
# | -------------- | ------------------------ | ------------------------------- |
# | Data Type      | list of lists            | NumPy array                     |
# | Slicing Syntax | same `[start:end]`       | same `[start:end]`              |
# | Shape          | need to compute manually | `.shape` attribute built-in     |
# | Speed          | slower for big data      | much faster                     |
# | Conversion     | stays as list            | need `.tolist()` to return list |


# rows, cols = np_array.shape  # only if array is 2D
# shape[0] → first axis (rows in a 2D array)
# shape[1] → second axis (columns in a 2D array)

#############