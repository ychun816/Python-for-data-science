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


# outer() Function (Closure / 外層函數) 閉包外層函式
def outer(
    x: Union[int, float],
    function: Callable[[Any], Any],
) -> Callable[[], float]:
    """Return a closure that applies `function` to progressively larger
    powers.

    Each call to the returned `inner()` increases an internal counter and
    applies `function(x ** count)`.
    """
    # Function receives an initial value x and a function to apply repeatedly
    # 外層函式收到初始值 x 和要重複應用的
    # functionCallable[[Callable[..., Any]], Callable[..., Any]]

    # keep an internal value that will be updated on each call
    current = x

    def inner() -> float:
        """Apply `function` to the current value, update it and return it.

        This matches the exercise requirement: each call applies the provided
        function to the previous result (first call applies it to `x`).
        """
        # Allows modification of outer variable / 允許修改 outer 的變數
        nonlocal current

        # Update the stored value by applying the passed function
        # 將 current 傳入 function，新結果再存回 current
        current = function(current)
        return current   # Return the new updated value / 回傳更新後的值

    # Return the closure / 回傳閉包（可被多次呼叫的函式物件）
    return inner

# TESTER ####
# from in_out import outer
# from in_out import square
# from in_out import pow


# my_counter = outer(3, square)
# print(my_counter())
# print(my_counter())
# print(my_counter())
# print("---")

# another_counter = outer(1.5, pow)
# print(another_counter())
# print(another_counter())
# print(another_counter())

# OUTPUT ##############
# $> python tester.py
# 9 81
# 6561
# ---
# 1.8371173070873836
# 3.056683336818703
# 30.42684786675409
# $>
