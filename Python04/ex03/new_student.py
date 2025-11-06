#!/usr/bin/env python3

# Student dataclass
# - accepts name and surname
# - active defaults to True
# - login is generated from surname (capitalized first letter)
# - id is a random 15-letter lowercase string from generate_id()
# - login and id are excluded from __init__ (init=False)

import random
import string

from dataclasses import dataclass, field


# Uses random.choices from string.ascii_lowercase.
# Returns a random 15-letter lowercase string.
def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)  # cannot be set in __init__
    id: str = field(init=False)     # cannot be set in __init__

    # Dataclasses provide __post_init__, which runs after the auto-generated
    # __init__. Use it to initialize login and id so they cannot be overridden
    # by caller-supplied keyword arguments.
    def __post_init__(self):
        self.login = self.surname.capitalize()  # capitalizes first letter
        self.id = generate_id()  # random ID
