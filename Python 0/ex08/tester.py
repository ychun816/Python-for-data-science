#!/usr/bin/env python3

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# recreated version
print("=== MY FUNC : ft_tqdm() ===")
for elem in ft_tqdm(range(333)):
sleep(0.005)
print()

# original built-in func
print("=== ORIGNIAL FUNC : tqdm() ===")
for elem in tqdm(range(333)):
sleep(0.005)
print()



#OUTPUT
# $> python tester.py
# 100%|[===============================================================>]| 333/333
# 100%| | 333/333 [00:01<00:00, 191.61it/s]