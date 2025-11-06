#!/usr/bin/env python3

from abc import ABC, abstractmethod


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
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Set the character's state to not alive (False)."""
        pass


class Stark(Character):
    """A Stark character, inheriting from Character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Stark character with first name and alive state.

        Args:
            first_name (str): Name of the Stark character.
            is_alive (bool, optional): Alive state. Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Set the Stark character's state to not alive (False)."""
        try:
            if self.is_alive:
                self.is_alive = False
        except AttributeError as e:
            print(f"Error: cannot change state - {e}")
