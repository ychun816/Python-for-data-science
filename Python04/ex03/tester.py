#! usr/bin/env python3

from new_student import Student


student = Student(name = "Edward", surname = "agle")

student = Student(name = "Edward", surname = "agle", id = "toto")

print(student)

#OUTPUT
#  (id is random)
# $> python tester.py
# Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
# $>

# $> python tester.py
# ...
# TypeError: Student.__init__() got an unexpected keyword argument 'id'
# $>


