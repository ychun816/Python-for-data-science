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
