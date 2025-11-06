#!/usr/bin/env python3

from S1E7 import Baratheon, Lannister, create_lannister


Robert = Baratheon("Robert")
print(Robert.__dict__)
print(str(Robert))
print(repr(Robert))
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(str(Cersei))
print(Cersei.is_alive)
print("---")
Jaine = create_lannister("Jaine", True)
print("Name:", Jaine.first_name, f"({type(Jaine).__name__})")
print("Alive:", Jaine.is_alive)


# OUTPUT (example)
# $> python tester.py
# {'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon'}
# True
# ---
# {'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister'}
# True
# Name : ('Jaine', 'Lannister'), Alive : True
# $>
