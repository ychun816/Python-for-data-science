#! usr/bin/env python3

# Create a decorator @callLimit(n) that:
# 1. limits how many times a function can be called,
# 2. after the limit is reached → it doesn’t run,
# 3. instead, it prints an error message like: Error: <function g at 0x7fabdc243ee0> call too many times


# decorator with parameter
# -> A decorator with parameter = function returning a decorator function.


def callLimit(limit: int):      # Layer 1: accepts the limit
    """Layer 1: accepts the limit"""
    count = 0                   # keeps track of how many times called

    def callLimiter(function):  # Layer 2: wraps the target function
        """Layer 2: wraps the target function"""
        
        def limit_function(*args: Any, **kwds: Any): # Layer 3: actual wrapper
            """Layer 3: actual wrapper"""
            nonlocal count # allow modification of outer variable
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times!")
        
        return limit_function # Layer 2: returns its wrapper
   
   return callLimiter  # Layer 1: returns the decorator