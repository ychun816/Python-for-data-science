#!/usr/bin/env python3

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """➽ Constructor for Baratheon.

        Initialize a Baratheon character.
        """
        super().__init__(first_name, is_alive)

        # Add family-specific attributes
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """➽ Method __str__(): return a human-readable string."""
        return f"{self.first_name} {self.family_name}"

    def __repr__(self):
        """Return the instance representation used by the tester."""
        return (
            f"Vector: ('{self.family_name}', "
            f"'{self.eyes}', '{self.hairs}')"
        )

    def die(self):
        """➽ Method die(): mark this Baratheon as not alive."""
        self.is_alive = False

    @classmethod
    def create(cls, first_name, is_alive=True):
        """➽ Class method create(): create a new Baratheon instance."""
        return cls(first_name, is_alive)


class Lannister(Character):
    """➽ Lannister class — a member of House Lannister.

    Class: Lannister
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """➽ Constructor for Lannister.

        Initialize a Lannister character.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """➽ Method __str__(): return a human-readable string."""
        return f"{self.first_name} {self.family_name}"

    def __repr__(self):
        """Return the instance representation used by the tester.

        See Baratheon.__repr__ for rationale.
        """
        return (
            f"Vector: ('{self.family_name}', "
            f"'{self.eyes}', '{self.hairs}')"
        )

    def die(self):
        """Method die(): mark this Lannister as not alive."""
        self.is_alive = False

    @classmethod
    def create(cls, first_name, is_alive=True):
        """➽ Class method create(): create a new Lannister instance."""
        return cls(first_name, is_alive)
    # Alias the `create` method to the tester-expected name.
    # Allows callers to use either `Lannister.create(...)` or
    # `Lannister.create_lannister(...)`.
    create_lannister = create

# Note: module-level factory `create_lannister` intentionally removed to keep
# the API minimal. Call `Lannister.create_lannister(...)` instead.

# NOTES ###
# __init__: constructor method to initialize object attributes.

# __str__(): human-readable string representation of the object.
# -> Used in print(object)
# -> Must return a readable string

# __repr__(): developer-readable representation of the object.
# -> Used in debugging / console inspections
# -> Must return a clear developer-style representation

# __dict__: attribute storage of an object.
# Inheritance: classes Baratheon and Lannister inherit from Character.

# super(): access parent class methods.
# is_alive: attribute to track if character is alive.
# die(): method to change the character's alive state.
# create(): class method to instantiate new objects.

# @classmethod: decorator to define class methods.
# -> first parameter is the class itself! NOT self (the instance)

# TESTER ###
# from S1E7 import Baratheon, Lannister, create_lannister

# Robert = Baratheon("Robert")
# print(Robert.__dict__)
# print(str(Robert))
# print(repr(Robert))
# print(Robert.is_alive)
# Robert.die()
# print(Robert.is_alive)
# print(Robert.__doc__)
# print("---")
# Cersei = Lannister("Cersei")
# print(Cersei.__dict__)
# print(str(Cersei))
# print(Cersei.is_alive)
# print("---")
# Jaine = create_lannister("Jaine", True)
# print("Name:", Jaine.first_name, f"({type(Jaine).__name__})")
# print("Alive:", Jaine.is_alive)
