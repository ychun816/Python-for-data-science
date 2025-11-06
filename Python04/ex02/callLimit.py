#!/usr/bin/env python3

"""
Decorator factory that limits how many times a function can be called.

The returned decorator allows a function to run `limit` times and then
prints an error message on subsequent calls.
"""

from typing import Any, Callable


def callLimit(
    limit: int,
) -> Callable[
    [Callable[..., Any]],
    Callable[..., Any],
]:
    """Layer 1: accepts the limit and returns a decorator.

    The returned decorator, when applied to a function, will allow that
    function to run `limit` times and then print an error message on
    subsequent calls.
    """
    count = 0

    def callLimiter(function: Callable[..., Any]) -> Callable[..., Any]:
        """Layer 2: the actual decorator wrapping `function`."""

        def limit_function(*args: Any, **kwds: Any) -> Any:
            """Layer 3: wrapper that enforces the call limit."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            print(f"Error: {function} call too many times!")

        return limit_function

    return callLimiter
