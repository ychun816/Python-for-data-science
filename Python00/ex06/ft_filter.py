#!/usr/bin/env python3

# define a function -> stores the instructions for later use
def ft_filter(function, iterable):
    """Return a list of elements from iterable where
    function(element) is True.
    """
    # Build and return a new list including items where
    # function(item) is True
    return [item for item in iterable if function(item)]


if __name__ == "__main__":
    # Example usage
    def is_even(x):
        return x % 2 == 0

    nbs = [1, 2, 3, 4, 5]
    print(ft_filter(is_even, nbs))

# OUTPUT
# $> python filterstring.py 'Hello the World' 4
# ['Hello', 'World']
# $>

# $> python filterstring.py 'Hello the World' 99
# []
# $>

# $> python filterstring.py 3 'Hello the World'
# AssertionError: the arguments are bad
# $>

# $> python filterstring.py
# AssertionError: the arguments are bad
# $>


# NOTES

# return [item for item in iterable if function(item)]
# -> "For every element in iterable, include it in a new list."

# if function(item)
# [item for item in iterable if function(item)]
# -> filter condition
# -> function(item) should return True or False
# -> Only include item in the new list if the function returns True.

# lambda -> creates an anonymous (unnamed) function

################################
