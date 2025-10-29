
from S1E9 import Character, Stark

def main():
    Ned = Stark("Ned")
    print(Ned.__dict__) # {'first_name': 'Ned', 'is_alive': True}
    print(Ned.is_alive) # True
    Ned.die()
    print(Ned.is_alive) # False
    print(Ned.__doc__) # Stark class docstring
    print(Ned.__init__.__doc__) # Constructor docstring
    print(Ned.die.__doc__) # die() docstring
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__) # {'first_name': 'Lyanna', 'is_alive': False}

if __name__ == "__main__":
    main()


# OUTPUT
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