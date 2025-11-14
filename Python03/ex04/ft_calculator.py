#!/usr/bin/env python3

# Decorators: using @staticmethod so methods can be called on the
# class without instantiation (e.g., calculator.dotproduct(a, b)).


class calculator:
    # --- Decorator: staticmethod ---
    # Allows calling these methods directly from the class.

    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        """Calculate dot product of two equal-sized vectors."""
        result = sum(x * y for x, y in zip(v1, v2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """Add two vectors element-wise."""
        # produce float results with one decimal place
        result = [float(x + y) for x, y in zip(v1, v2)]
        # match subject formatting (space before colon)
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """Subtract two vectors element-wise."""
        result = [float(x - y) for x, y in zip(v1, v2)]
        print(f"Sous Vector is: {result}")

# NOTES ###
# @staticmethod: 
# - The method does NOT take self
# - The method does NOT depend on instance data
# - The method belongs to the class, not the instance
# A decorator that defines a method as a static method,
# meaning it can be called on the class itself without needing an instance.
# list[float]: A type hint indicating a list of floating-point numbers.
# zip(): A built-in function that aggregates elements from multiple iterables.
# sum(): A built-in function that returns the sum of a sequence of numbers.
# float(): A built-in function that converts a value to a floating-point number.
# element-wise: Performing operations on corresponding elements of two sequences.
