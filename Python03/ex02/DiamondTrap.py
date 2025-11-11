#!/usr/bin/env python3

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Joffrey Baratheon – a hybrid king between Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize King Joffrey with mixed family traits."""
        super().__init__(first_name, is_alive)
        # Do not create private attributes here; rely on the public
        # attributes (`eyes`, `hairs`) that the parent constructors set.
        # Property getters/setters below operate on the public keys so the
        # object's `__dict__` matches the expected shape.

    # ---- Using @property ----
    @property
    def eyes(self):
        """Return current eye color."""
        return self.__dict__.get("eyes")

    @eyes.setter
    def eyes(self, color):
        """Set eye color safely."""
        # Update the public attribute so __dict__ reflects the change.
        self.__dict__["eyes"] = color

    @property
    def hairs(self):
        """Return current hair color."""
        return self.__dict__.get("hairs")

    @hairs.setter
    def hairs(self, color):
        """Set hair color safely."""
        self.__dict__["hairs"] = color

    # ---- Extra getter/setter for backward compatibility ----
    def set_eyes(self, color):
        """Public setter for eyes (legacy wrapper)."""
        self.eyes = color

    def set_hairs(self, color):
        """Public setter for hairs (legacy wrapper)."""
        self.hairs = color

    def get_eyes(self):
        """Public getter for eyes."""
        return self.eyes

    def get_hairs(self):
        """Public getter for hairs."""
        return self.hairs
