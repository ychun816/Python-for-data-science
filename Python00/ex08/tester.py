#!/usr/bin/env python3

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main() -> None:

    # recreated version
    print("=== MY FUNC : ft_tqdm() ===")
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    # original built-in func
    print("=== ORIGINAL FUNC : tqdm() ===")
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()


# OUTPUT
# Example run (truncated):
# $> python tester.py
# 100%|[=========================================>]| 333/333
# 100%| | 333/333 [00:01<00:00, 191.61it/s]
