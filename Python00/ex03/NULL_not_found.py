#!/usr/bin/env python3

#prototype
def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object, type(object))
    elif isinstance(object, float) and object != object:  # NaN check
        print("Cheese:", object, type(object))
    elif object == 0:
        print("Zero:", object, type(object))
    elif object == '':
        print("Empty:", object, type(object))
    elif object is False:
        print("Fake:", object, type(object))
    else:
        print("Type not Found")
        return 1 #for unknown types
    return 0 #success


#### NOTES ######################

# (object: any) → input parameter with type hint (any = anything)

# is → checks identity (used for None and False)
# object != object → only NaN is not equal to itself, so it identifies NaN.
# object == 0 → integer zero check
# object == '' → empty string check.
# return 1 → for unknown types


# ==	(Equality):	Whether two values are the same in value
# → == can be overridden by custom objects (__eq__ method)
# is	(Identity):	Whether two objects are the exact same object in memory
# object is True
# object is False
################################

