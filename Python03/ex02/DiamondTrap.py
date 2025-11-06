#!/usr/bin/env python3

"""Minimal King implementation for ex02.

This module provides a simple King class that inherits from
Baratheon and Lannister (imported from S1E7). It exposes
properties for eyes and hairs with safe getters/setters.
"""

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A simple hybrid King combining Baratheon and Lannister.

    This class keeps private attributes for eyes and hairs and
    exposes property accessors and small compatibility wrappers.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        # Let parent initializers run according to MRO
        super().__init__(first_name, is_alive)
        # default values if parents didn't set them
        self._eyes = getattr(self, "eyes", "brown")
        self._hairs = getattr(self, "hairs", "dark")

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

    # compatibility wrappers
    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hairs = color

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
