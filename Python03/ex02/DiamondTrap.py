#! usr/bin/env python3

# 1. Inherit from both Baratheon and Lannister.
# 2. Use @property and setter methods to safely access and modify attributes like eyes and hairs.
# 3. Understand Python’s MRO (Method Resolution Order) — which parent gets called first.

from abc import ABC, abstractmethod
from S1E7 import Baratheon, Lannister

from abc import ABC, abstractmethod

# abstract class 
# class Character(ABC):
#     """Abstract base class for all characters in GOT."""
#     def __init__(self, first_name, is_alive=True):
#         """Initialize character with name and life status."""
#         self.first_name = first_name
#         self.is_alive = is_alive

#     @abstractmethod
#     def die(self):
#         """Abstract method to kill the character."""
#         pass



class King(Baratheon, Lannister):
    """Joffrey Baratheon – A hybrid king between Baratheon and Lannister."""

    def __init(self, first_name:str, is_alive:bool=true):
        """Initialize King Joffrey with mixed family traits."""
        super().__init__(first_name, is_alive)
        # The Baratheon __init__() runs first (due to MRO)
        # So by default, eyes="brown", hairs="dark"
        # But we can customize later with setters.

    # ---- Using @property ----
    @property
    def eyes(self):
        """Return current eye color."""
        return self._eyes

    @eyes.setter #Property decorator defines how we safely set a private variable
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
    #setter 
    def set_eyes(self, color):  #A wrapper method around the property for legacy-style setter calls
        """Public setter for eyes."""
        self.eyes = color

    def set_hairs(self, color):
        """Public setter for hairs."""
        self.hairs = color

    #getter
    def get_eyes(self):
        """Public getter for eyes."""
        return self.eyes


    def get_hairs(self):
        """Public getter for hairs."""
        return self.hairs


