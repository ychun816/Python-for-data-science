#! usr/bin/env python3

# Import ABC and abstractmethod from the abc module.
# ABC is the base for creating abstract base classes.
# abstractmethod is a decorator used to mark methods that subclasses must implement.
from abc import ABC, abstractmethod

# abstract base mother class
class Character(ABC):
    """Abstract base class representing a generic character in a story.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): The living state of the character. Defaults to True.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
    """Initialize a Character with a first name and optional alive state.

    Args:
        first_name (str): Name of the character.
        is_alive (bool, optional): Alive state. Defaults to True.
    """
    # Constructor (initializer) for Character instances.
    # 'first_name' is a required positional argument.
    # 'is_alive' is optional and defaults to True.
    self.first_name = first_name      # Store the provided first_name on the instance as an attribute.
    self.is_alive = is_alive          # Store the provided is_alive boolean on the instance as an attribute.

    @abstractmethod
        def die(self):
        """Set the character's state to not alive (False)."""
        # The abstract method die() is declared here.
        # Subclasses MUST implement this method; attempting to instantiate
        # Character directly will raise a TypeError because die is abstract.
        pass
        # pass is required syntactically because the method has no implementation
        # in the abstract base class; it only defines the signature and docstring.


#inherit class
class Stark(Character):
    """A Stark character, inheriting from Character."""
    def __init__(self, first_name: str, is_alive: bool = True):
    """Initialize a Stark character with first name and alive state.

    Args:
        first_name (str): Name of the Stark character.
        is_alive (bool, optional): Alive state. Defaults to True.
    """
    # Stark's constructor mirrors Character's signature and passes values up.

    # Call parent class (Character) initializer to set shared attributes.
    # Using super() avoids duplicating initialization logic.
    super().__init__(first_name, is_alive)

    def die(self):
        """Set the Stark character's state to not alive (False)."""
        # Concrete implementation of the abstract method die().
        # This method changes the is_alive attribute to False.
        try:
            # will invalidate the exercises" — catching attribute errors is defensive.
            if self.is_alive:
                self.is_alive = False                 # Only change the state if the character is currently alive.

        except AttributeError as e:
            # If for some reason the instance does not have is_alive attribute,
            # catch the AttributeError and print a helpful message rather than
            # letting the exception propagate uncaught.
            print(f"Error: cannot change state - {e}")
