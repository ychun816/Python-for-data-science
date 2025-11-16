#!/usr/bin/env python3

"""
Decorator factory that limits how many times a function can be called.

The returned decorator allows a function to run `limit` times and then
prints an error message on subsequent calls.
"""

# Any: any type # Callable: type hint for functions
from typing import Any, Callable


# LAYER 1: Decorator factory ############################################
def callLimit(
    limit: int,
) -> Callable[
    [Callable[..., Any]],
    Callable[..., Any],
    # A function that receives a function → returns another function
]:
    """Layer 1: accepts the limit and returns a decorator.

    The returned decorator, when applied to a function, will allow that
    function to run `limit` times and then print an error message on
    subsequent calls.
    """
    # A closure variable to keep track of the number of calls
    # Stored inside callLimit so each decorated function gets its own counter
    count = 0

    # LAYER 2: Decorator #################################################
    def callLimiter(function: Callable[..., Any]) -> Callable[..., Any]:
        """Layer 2: the actual decorator wrapping `function`."""

        # LAYER 3: Wrapper #################################################
        # Takes any positional/keyword arguments
        # This lets the decorator work with any function signature
        def limit_function(*args: Any, **kwds: Any) -> Any:
            """Layer 3: wrapper that enforces the call limit."""
            # Allows modifying the count variable from Layer 1
            # Without nonlocal, Python treat count as new local variable
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)  # Call og function
            # Match subject output: no trailing punctuation after the message
            print(f"Error: {function} call too many times")

        return limit_function  # End of Layer 3: return the wrapper #######

    return callLimiter  # End of Layer 2: return the decorator #############

# NOTES ###
# Decorator factory: A function that returns a decorator.

# callLimit(limit): Accepts an integer limit and returns a decorator.
# callLimit = Layer 1: the decorator factory
# It takes one argument: limit (maximum number of allowed calls)
# It returns a decorator (callLimiter)

# callLimiter(function): The actual decorator that wraps the target function.
# limit_function(*args, **kwds): The wrapper function that enforces call limit.
# nonlocal count: Allows modification of `count` variable frm enclosing scope.

# TESTER ####
# from callLimit import callLimit


# @callLimit(3)
# def f():
#     print("f()")


# @callLimit(1)
# def g():
#     print("g()")


# for i in range(3):
#     f()
#     g()

# OUTPUT
# f()
# g()
# f()
# Error: <function g at 0x7fabdc243ee0> call too many times
# f()
# Error: <function g at 0x7fabdc243ee0> call too many times
# $>
