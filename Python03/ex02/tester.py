#!/usr/bin/env python3

from DiamondTrap import King


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

# OUTPUT ###
# {'first_name': 'Joffrey', 'is_alive': True, 'family_name':
#  'Baratheon', 'eyes': 'brown', 'hair': 'dark'}
# blue
# light
# {'first_name': 'Joffrey', 'is_alive': True, 'family_name':
#  'Baratheon', 'eyes': 'blue', 'hairs': 'light'}

# Note: since Python 2.3 the language uses C3 linearization to handle
# multiple inheritance ordering in diamond patterns.
