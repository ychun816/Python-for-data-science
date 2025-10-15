#!/usr/bin/env python3

#subject
#prototype
def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print("List : ", type(object))
    elif isinstance(object, tuple):
        print("Tuple : ", type(object))
    elif isinstance(object, set):
        print("Tuple : ", type(object))
    elif isinstance(object, dict):
        print("Tuple : ", type(object))
    elif isinstance(object, str):
        print(f"{object} is a string : {type(object)}")
    else:
        print("this type not found")
    return 42 






#### NOTES ######################

# (object: any)
# parameter named object, with a type hint saying it can be any type
# -> int 
# means it returns an integer (in this case, always 42)



# type(obj) → returns the type itself
# isinstance(obj, class) → returns True if the object is of that type (or inherits from it)

# Control flow (if / elif / else)
# isinstance(value, type_or_tuple)
# Returns True if value is an instance of type_or_tuple.


# object -> a placeholder
# type(object) : Built-in function that returns the actual type object of the variable. Example: <class 'list'>.
# , in print("List : ", type(object)) : Separates multiple items in one print call. Python automatically adds a space between them.

################################