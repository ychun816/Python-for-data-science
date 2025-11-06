#!/usr/bin/env python3

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Joffrey Baratheon – a hybrid king between Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize King Joffrey with mixed family traits."""
        super().__init__(first_name, is_alive)

    # ---- Using @property ----
    @property
    def eyes(self):
        """Return current eye color."""
        return self._eyes

    @eyes.setter
    def eyes(self, color):
        """Set eye color safely."""
        self._eyes = color

    @property
    def hairs(self):
        """Return current hair color."""
        return self._hairs

    @hairs.setter
    def hairs(self, color):
        """Set hair color safely."""
        self._hairs = color

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
