#! usr/bin/env python3

from ft_calculator import calculator

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5 # → add 5 to each element → prints new vector

Print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0]) 
v2 * 5 # → multiply each element by 5 → prints new vector

Print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5  # → subtract 5 from each element
v3 / 5  # → divide each element by 5


#OUTPUT
# $> python tester.py
# [5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
# ---
# [0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
# ---
# [5.0, 10.0, 15.0]
# [1.0, 2.0, 3.0]
# $>