#!/usr/bin/env python3

# TEST 1 ####
from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)

# TEST 2 ####
# from new_student import Student


# student = Student(name = "Edward", surname = "agle", id = "toto")
# print(student)


# OUTPUT 1 (id is random)###
# $> python tester.py
# Student(name='Edward', surname='agle', active=True,
# login='Eagle', id='trannxhndgtolvh')
# $>

# OUTPUT 2 (id is random, login cannot be set)###
# $> python tester.py
# ...
# TypeError: Student.__init__() got an unexpected keyword argument 'id'
# $>
