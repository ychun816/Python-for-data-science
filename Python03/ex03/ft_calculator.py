#! usr/bin/env python3

# create a calculator class that represents a vector (a list of numbers) and can perform math operations with a scalar (single number).
# Each operation should modify and print the new vector.

class calculator:
    """A calculator class that performs scalar operations on a vector."""

    #init 
    def __init__(self, vector) -> None:
        """Initialize with a list (vector) of floats."""
        self.vector = vector

    #add
    def __add__(self, scalar) -> None:
        """Add scalar to each element and print result."""
        result = [x + scalar for x in self.vector]
        print (result)
        return result

    #multiple
    def __mul__(self, scalar) -> None:
        """Multiply each element by scalar and print result."""
        result = [x * scalar for x in self.vector]
        print (result)
        return result

    #substract
    def __sub__(self, scalar) -> None:
        """Subtract scalar from each element and print result."""
        result = [x - scalar for x in self.vector]
        print (result)
        return result

    #divide
    def __truediv__(self, scalar) -> None:
        """Divide each element by scalar and print result (handle div by 0)."""
        if scalar == 0:
            print("Error: Cannot devide by zero.")
            return None
        result = [x / scalar for x in self.vector]
        print(result)
        return result