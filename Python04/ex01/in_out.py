#!/usr/bin/env python3

"""Small module demonstrating closures used by the exercises.

Provides `square`, `pow` and `outer` (which returns a closure).
"""

from typing import Any, Callable, Union


# square(x) – 平方
def square(x: Union[int, float]) -> Union[int, float]:
    """Return x squared (x^2)."""
    return x * x


# pow(x) – 自身的次方 (multiply x by itself x times)
def pow(x: Union[int, float]) -> Union[int, float]:
    """Return x to the power of x (x ** x)."""
    return x ** x


# outer() Function (Closure / 外層函數)
def outer(
    x: Union[int, float],
    function: Callable[[Any], Any],
) -> Callable[[], float]:
    """Return a closure that applies `function` to progressively larger
    powers.

    Each call to the returned `inner()` increases an internal counter and
    applies `function(x ** count)`.
    """
    inner_count = 0  # keep track of how many times inner is called

    def inner() -> float:
        """Uses the x and inner_count from outer()
        even after outer() finished.
        """
        nonlocal inner_count
        inner_count += 1
        result = function(x ** inner_count)
        return result

    return inner


# EXAMPLES (commented out)

# my_counter = outer(3, square)
# print(my_counter())
# print(my_counter())
# print(my_counter())

# another_counter = outer(1.5, pow)
# print(another_counter())
# print(another_counter())
# print(another_counter())
