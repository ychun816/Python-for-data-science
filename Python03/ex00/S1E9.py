#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Character(ABC):
    """Character class — abstract base for characters in a story.

    Class: Character

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): The living state of the character. Defaults to True.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Character.

        Initialize a Character with a first name and optional alive state.

        Args:
            first_name (str): Name of the character.
            is_alive (bool, optional): Alive state. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """➽ Method die(): set the character's state to not alive (False)."""
        pass


class Stark(Character):
    """➽ Stark class — a specific Character implementation.
    Class: Stark
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """➽ Stark Constructor:
        Initialize a Stark character with first name and alive state.
        Args:
            first_name (str): Name of the Stark character.
            is_alive (bool, optional): Alive state. Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """➽ Method die(): set the Stark character's state to not alive.

        This implements the abstract `die` method from `Character` and
        sets ``is_alive`` to ``False``.
        """
        try:
            if getattr(self, "is_alive", False):
                self.is_alive = False
        except AttributeError as e:
            print(f"Error: cannot change state - {e}")

# NOTES ###
# Abstract Base Classes (ABC): marks it as an abstract base class.
# -Cannot be instantiated.
# - Exist to define required behavior for subclasses.
# @abstractmethod ensures every subclass must implement the method die()
# self: the instance itself.
# __init__: is the constructor method, where set initial attributes for object
# super(): gives access to the parent class methods
# super().__init__(first_name, is_alive)
# -> call the parent class (Character) constructor
# -> so it can initialize the attributes defined there

# TESTER.PY ###
# from S1E9 import Stark


# def main():
#     Ned = Stark("Ned")
#     print(Ned.__dict__)  # {'first_name': 'Ned', 'is_alive': True}
#     print(Ned.is_alive)  # True
#     Ned.die()
#     print(Ned.is_alive)  # False
#     print(Ned.__doc__)  # Stark class docstring
#     print(Ned.__init__.__doc__)  # Constructor docstring
#     print(Ned.die.__doc__)  # die() docstring
#     print("---")
#     Lyanna = Stark("Lyanna", False)
#     print(Lyanna.__dict__)  # {'first_name': 'Lyanna', 'is_alive': False}


# if __name__ == "__main__":
#     main()

# OUTPUT ###
# $> python tester.py
# {'first_name': 'Ned', 'is_alive': True}
# True
# False
# Your docstring for Class
# Your docstring for Constructor
# Your docstring for Method
# ---
# {'first_name': 'Lyanna', 'is_alive': False}
# $>

# Make sure you have used an abstract class, the code below should make
# an error.
# from S1E9 import Character
# hodor = Character("hodor")
# TypeError: Can't instantiate abstract class Character with abstract method
# $>
