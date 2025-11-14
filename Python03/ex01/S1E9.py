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
