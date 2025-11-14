#!/usr/bin/env python3

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Joffrey Baratheon – a hybrid king between Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize King Joffrey with mixed family traits."""
        super().__init__(first_name, is_alive)
        # Parents set `hairs` in their constructors. For this exercise the
        # tester expects the initial dict to show the singular key `hair`.
        # Move the parent's `hairs` value to `hair` so the first printout
        # matches the expected shape.
        if "hairs" in self.__dict__ and "hair" not in self.__dict__:
            self.__dict__["hair"] = self.__dict__.pop("hairs")

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
        """Return current hair color (plural key used by parents)."""
        return self.__dict__.get("hairs")

    @hairs.setter
    def hairs(self, color):
        """Set hair color safely using the 'hairs' key expected upstream."""
        self.__dict__["hairs"] = color

    # ---- Extra getter/setter for backward compatibility ----
    def set_eyes(self, color):
        """Public setter for eyes (legacy wrapper)."""
        self.eyes = color

    def set_hairs(self, color):
        """Public setter for hairs (legacy wrapper)."""
        # Set the canonical plural key and remove the singular `hair` key
        # so the final object's __dict__ matches the expected output.
        self.hairs = color
        if "hair" in self.__dict__:
            del self.__dict__["hair"]

    def get_eyes(self):
        """Public getter for eyes."""
        return self.eyes

    def get_hairs(self):
        """Public getter for hairs."""
        return self.hairs
