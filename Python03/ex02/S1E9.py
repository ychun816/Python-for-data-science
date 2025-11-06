#!/usr/bin/env python3

"""Simple Character/ Starks for ex02.

Provide a minimal abstract Character base class and a concrete
Stark subclass with a working die() method.
"""

from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a generic character.

    Attributes:
        first_name (str): The character's first name.
        is_alive (bool): Whether the character is alive. Defaults to True.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Mark the character as not alive."""
        raise NotImplementedError


class Stark(Character):
    """A Stark character, concrete implementation of Character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)

    def die(self):
        """Set the Stark instance as dead (is_alive = False)."""
        if self.is_alive:
            self.is_alive = False
