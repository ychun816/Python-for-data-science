#!/usr/bin/env python3

from new_student import Student


student = Student(name="Edward", surname="agle")

print(student)

# OUTPUT
# (id is random)
# Example run (formatted):
# Student(name='Edward', surname='agle', active=True,
#         login='Eagle', id='trannxhndgtolvh')
#
# If you pass id into the constructor you should see a TypeError:
# Student.__init__() got an unexpected keyword argument 'id'
