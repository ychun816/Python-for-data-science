
from S1E9 import Character

class Baratheon(Character):
    """A class representing a member of House Baratheon."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)

        # Add family-specific attributes
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    

    def __str__(self):
        """Return a human-readable string version of the object."""
        return f"{self.first_name} {self.family_name}"   # When you use print(obj), __str__ is called.

    def __repr__(self):
        """Return a developer-readable representation of the object."""
        return f"<Character: {self.first_name} {self.family_name}>"         # When you type obj in the console, __repr__ is used.

    @classmethod
    def create(cls, first_name, is_alive=True):
        """Class method to create a new Baratheon instance."""
        return cls(first_name, is_alive)  # cls represents the class itself (Baratheon)
        # This allows chained creation, like: Baratheon.create("Robert").create(...)


class Lannister(Character):
    """A Lannister character, inheriting from Character."""
    def __init__(self, first_name:str, is_alive:bool = true):
        """Initialize a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

        def __str__(self):
            """Return a human-readable string version of the object."""
            return f"{self.first_name} {self.family_name}"
        
        def __repr__(self):
            """Return a developer-readable representation of the object."""
            return f"<Character: {self.first_name} {self.family_name}>"

        @classmethod
        def create(cls, first_name, is_alive=True):
            """Class method to create a new Lannister instance."""
            return cls(first_name, is_alive)

# --- Decorator function example (optional bonus task in spec) ---
# Instead of calling Lannister(first_name), we use a helper decorator-like function.
def create_lannister(your code here):
    """Function that creates a Lannister character easily."""
    return Lannister(first_name, is_alive)
