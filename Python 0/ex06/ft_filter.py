#!/usr/bin/env python3


# define a function -> tores the instructions for later use
def ft_filter(function, iterable):
    """Return a list of elements from iterable where function(element) is True."""
    return [item for item in literable if function(item)] #=> function(item) #-> is_even(item)

    is_even = lambda x: x % 2 == 0
    numbers = [1, 2, 3, 4, 5]

    print(ft_filter(is_even, numbers))  # [2, 4]

#the actual usage of the function
#They call ft_filter with real values
is_even = lambda x: x % 2 == 0
nbs = [1, 2, 3, 4, 5]
print(ft_filter(is_even, nbs))

#OUTPUT
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


#### NOTES ######################

# return [item for item in iterable if function(item)]
# -> “For every element in iterable, include it in a new list.”

# if function(item)
# [item for item in iterable if function(item)]
# -> filter condition
# -> function(item) should return True or False
# -> Only include item in the new list if the function returns True.


# lambda → creates an anonymous (unnamed) function

################################