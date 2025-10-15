#!/usr/bin/env python3

# Generators (using yield)
# Dynamic terminal output (progress bar)

# ft_tqdm(range(333)) is a generator, not a list
def ft_tqdm(lst: range) -> None:
    """ 
    Recreates the tqdm loading bar using a generator and yield.
    Displays progress in the same line as it iterates. 
    """

    #calculate the nb of elements in a list
    total_elems = len(lst)

    #loop to enumerate(lst, start=1) -> give both the index (i) and the element (elem)
    for i, elem in enumerate(lst, start=1):
        
        # Calculate progress ratio (0.0 → 1.0) -> progress / total nb of elements
        progress_percent = i / total_elems 

        # Bar width and filled part
        bar_len = 50  # total characters in the progress bar
        to_fill = int(50 * progress_percent) #Calculates how many blocks of the bar should be “filled”

        # Print formatted progress bar on same line
        bar = "=" * to_fill + ">" + " " * (bar_len - to_fill) 
        print(f"\r{int(progress_percent * 100)}%|[{bar}]| {i}/{total_elems}", end="")

        # Yield current element so loop continues
        yield elem



### NOTES ###

# yield → Generator
# - a function that produces a sequence of values one at a time
# - it doesn’t store all elements, it produces them as you loop
# - (like return, but resumable)



# end="\r"
# Keeps updating on the same line (carriage return)

# f-string 
# formatting
# Clean, readable inline string formatting: f"{variable}"

# len(range(...))
# Get total count of items to calculate progress

# enumerate()
# Loops with both index and value (like C++ for (int i=0; ...))
# EX:
# lst = range(3)
# i=1, elem=0
# i=2, elem=1
# i=3, elem=2

# \r 
# moves the cursor to the beginning of the same line, 
# so the next print overwrites the previous one

# int(percent * 100) 
# shows the progress percentage as a whole number

# Iteration 1: "\r 0%|[>                                                 ]| 0/100"
# Iteration 2: "\r25%|[============>                                     ]| 25/100"
# Iteration 3: "\r50%|[=========================>                        ]| 50/100"
# Iteration 4: "\r75%|[=====================================>            ]| 75/100"
# Iteration 5: "\r100%|[=================================================>]| 100/100"


# 25%|[============>                                     ]| 25/100
# ↑
# cursor returns here before printing again

#############