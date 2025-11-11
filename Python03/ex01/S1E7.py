#!/usr/bin/env python3

from S1E9 import Character


class Baratheon(Character):
    """Baratheon class — a member of House Baratheon.

    Class: Baratheon
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Baratheon.

        Initialize a Baratheon character.
        """
        super().__init__(first_name, is_alive)

        # Add family-specific attributes
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Method __str__(): return a human-readable string."""
        return f"{self.first_name} {self.family_name}"

    def __repr__(self):
        """Method __repr__(): return a developer-readable representation."""
        return f"<Character: {self.first_name} {self.family_name}>"

    def die(self):
        """Method die(): mark this Baratheon as not alive."""
        self.is_alive = False

    @classmethod
    def create(cls, first_name, is_alive=True):
        """Class method create(): create a new Baratheon instance."""
        return cls(first_name, is_alive)


class Lannister(Character):
    """Lannister class — a member of House Lannister.

    Class: Lannister
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Lannister.

        Initialize a Lannister character.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Method __str__(): return a human-readable string."""
        return f"{self.first_name} {self.family_name}"

    def __repr__(self):
        """Method __repr__(): return a developer-readable representation."""
        return f"<Character: {self.first_name} {self.family_name}>"

    def die(self):
        """Method die(): mark this Lannister as not alive."""
        self.is_alive = False

    @classmethod
    def create(cls, first_name, is_alive=True):
        """Class method create(): create a new Lannister instance."""
        return cls(first_name, is_alive)


# Helper function to create a Lannister instance easily.
def create_lannister(first_name, is_alive=True):
    """Function create_lannister(): create a Lannister character easily."""
    return Lannister(first_name, is_alive)
