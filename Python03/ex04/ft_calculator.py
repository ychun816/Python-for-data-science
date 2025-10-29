#! usr/bin/env python3

# decorators → specifically @staticmethod -> allow you to call a method on the class without creating an object.
# 1. Create a class calculator
# 2. Perform dot product, vector addition, and vector subtraction
# 3. Without instantiating the class (so you call directly like calculator.dotproduct(a, b))

# cannot do:
# v = calculator([1, 2, 3])
# v.dotproduct([4, 5, 6])   # ❌ Not allowed

# must do:
# calculator.dotproduct([1, 2, 3], [4, 5, 6])  # ✅ OK

#class
class calculator:
    # --- Decorator: staticmethod ---
    # Allows us to call this method directly from the class
    
    # dot -> multiple
    @staticmethod
    def dotproduct(v1:list[float], V2: list[float]) -> None:
        """Calculate dot product of two equal-sized vectors"""
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")
    
    #add 
    @staticmethod
    def add_vec(v1:list[float], V2: list[float]) -> None:
        """Add two vectors element-wise"""
        result = [x + y for x, y in zp(V1, V2)]
        print(f"Add Vector is: {result}")
    
    #sous -> substract 
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """"Subtract two vectors element-wise"""
        result = [x - y for x, y in zp(V1, V2)]
        print(f"Add Vector is: {result}")


