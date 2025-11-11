#!/usr/bin/env python3

from S1E9 import Character


class Baratheon(Character):
    """A class representing a member of House Baratheon."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)

        # Add family-specific attributes
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a human-readable string version of the object."""
        return f"{self.first_name} {self.family_name}"

    def __repr__(self):
        """Return a developer-readable representation of the object."""
        return f"<Character: {self.first_name} {self.family_name}>"

    def die(self):
        """Method die(): mark this Baratheon as not alive."""
        self.is_alive = False

    @classmethod
    def create(cls, first_name, is_alive=True):
        """Class method to create a new Baratheon instance."""
        return cls(first_name, is_alive)


class Lannister(Character):
    """A Lannister character, inheriting from Character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return a human-readable string version of the object."""
        return f"{self.first_name} {self.family_name}"

    def __repr__(self):
        """Return a developer-readable representation of the object."""
        return f"<Character: {self.first_name} {self.family_name}>"

    def die(self):
        """Method die(): mark this Lannister as not alive."""
        self.is_alive = False

    @classmethod
    def create(cls, first_name, is_alive=True):
        """Class method to create a new Lannister instance."""
        return cls(first_name, is_alive)


# Helper function to create a Lannister instance easily.
def create_lannister(first_name, is_alive=True):
    """Function that creates a Lannister character easily."""
    return Lannister(first_name, is_alive)
