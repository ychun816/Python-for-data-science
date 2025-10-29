#! usr/bin/env python3

# Need a Student class that:
# 1. Accepts name and surname as input arguments.
# 2. Sets active = True by default.
# 3. Generates a login from the surname (capitalized first letter).
# 4. Generates a random 15-letter ID using generate_id().
# 5. Prevents login and id from being set in __init__ (should raise TypeError if attempted).


import random
import string

from dataclasses import dataclass, field


# Uses 'random.choices' from 'string.ascii_lowercase'
# Returns random 15-letter lowercase string.
def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))


# active has a default, so it can be omitted in __init__.
# field(init=False) → exclude from __init__.

@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False) # cannot be set in __init__
    id: str = field(init=False)     # cannot be set in __init__

    # Dataclasses allow __post_init__ -> runs after the auto-generated __init__
    # login and id are automatically set and cannot be overridden during initialization
    def __post_init__(self):
        self.login = self.surname.capitalize() #capitalizes first letter of surname.
        self.id = generate_id() #random ID
    