#!/usr/bin/env python3

import sys
import ft_filter

def main():
    """Filter words from string that are longer than N."""

    #check arg num
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    #assign args
    arg_str = sys.argv[1]
    arg_n = sys.argv[2]

    try:
        N = int(arg_n) #cover to int
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    #Split string into words
    words_list = arg_str.split()

    #Define a lambda for readability
    is_longer = lambda w: len(w) > N

    #Use list comprehension to filter
    filter_words = ft_filter.ft_filter(is_longer, words_list)
    # filter_words = [word for word in words_list if is_longer(word)]  
    print(filter_words)



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")



### NOTES ###

# ft_filter → refers to the module (the whole file)
# ft_filter.ft_filter → refers to the function inside that module

# function_name(argument1, argument2)
# -> ft_filter → the function you defined (your custom version of Python’s built-in filter())
# -> is_longer(arg1) → another function, passed as data (not called yet!)
# -> words_list(arg2) → the list you want to filter

# def ft_filter(function, iterable):
#     return [item for item in iterable if function(item)]
# -> take each item in iterable
# -> call function(item) (for example, is_longer(item))
# -> if it returns True, keep it in the list
#############