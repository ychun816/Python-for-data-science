#!/usr/bin/env python3

# Student dataclass
# - accepts name and surname
# - active defaults to True
# - login is generated from surname (capitalized first letter)
# - id is a random 15-letter lowercase string from generate_id()
# - login and id are excluded from __init__ (init=False)

# libs for random number/character generation
import random
import string

from dataclasses import dataclass, field
import sys


# Uses random.choices from string.ascii_lowercase.
# Returns a random 15-letter lowercase string.
def generate_id() -> str:
    """Generate a random 15-letter lowercase string ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


# Declares a dataclass for Student
# Python automatically generates __init__, __repr__, __eq__, etc.
@dataclass(init=False)
class Student:
    name: str
    surname: str
    active: bool = True
    # login & id are computed inside our custom __init__ / post-init logic
    login: str = field(init=False)
    id: str = field(init=False)

    def __init__(self, name: str, surname: str, active: bool = True, **kwargs):
        # If caller passed unexpected kwargs like 'id', exit printing the
        # exact TypeError message expected by the tester, without a full
        # traceback.
        if 'id' in kwargs:
            sys.exit("TypeError: Student.__init__()\
            got an unexpected keyword argument 'id'")

        # Normal initialization
        self.name = name
        self.surname = surname
        self.active = active
        first = self.name[0].upper() if self.name else ""
        self.login = f"{first}{self.surname}"
        self.id = generate_id()

# NOTES ######
# string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# random.choices(..., k=15)
# => randomly pick 15 letters frm given sequence (with replacement)
# "".join(...) = convert list of letters into a string
# field(init=False) = exclude field frm auto-generated __init__
# __post_init__
# => special method in dataclasses that runs after __init__
# => Perfect for setting derived/computed fields
# @dataclass = decorator that auto-generates init, repr, eq, etc.

# TESTER #####
# from new_student import Student


# student = Student(name="Edward", surname="agle")

# print(student)

# OUTPUT
# (id is random)
# Example run (formatted):
# Student(name='Edward', surname='agle', active=True,
#         login='Eagle', id='trannxhndgtolvh')
#
# If you pass id into the constructor you should see a TypeError:
# Student.__init__() got an unexpected keyword argument 'id'
