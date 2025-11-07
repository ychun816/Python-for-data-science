#!/usr/bin/env python3

"""Simple demo of Python container types.

This script places example code in main() to avoid module-level globals
and side effects at import time.
"""


def main() -> None:
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    # Modify values locally inside main (no module-level globals)
    ft_list[1] = "World!"
    ft_tuple = (ft_tuple[0], "France!")
    ft_set = {"Hello", "Paris!"}
    ft_dict["Hello"] = "42Paris!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


# if run as script, call main()
if __name__ == "__main__":
    main()

# OUTPUT
# $> python Hello.py | cat -e
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$
# $>

# NOTES ###
# sys lib: https://docs.python.org/3/library/sys.html

# Data types summary #
#
# List
# - Syntax: ["Hello", "World!"]
# - Ordered: Yes
# - Mutable: Yes
# - Allows duplicates: Yes
# - Access / modify: By index → list[0]
#   Change element: list[1] = "Hi"
#
# Tuple
# - Syntax: ("Hello", "France!")
# - Ordered: Yes
# - Mutable: No (immutable)
# - Allows duplicates: Yes
# - Access / modify: By index → tuple[0]; to change, create a new tuple
#
# Set
# - Syntax: {"Hello", "Paris!"}
# - Ordered: No (insertion order is preserved in CPython
#   implementations but conceptually unordered)
# - Mutable: Yes
# - Allows duplicates: No (only unique elements)
# - Access / modify:
#   Check membership: "Hello" in my_set
#   Add element: my_set.add("new")
#
# Dict
# - Syntax: {"Hello": "42Paris!"}
# - Ordered: Yes (as of Python 3.7+, insertion order is preserved)
# - Mutable: Yes
# - Allows duplicates: Keys must be unique; values can be duplicated
# - Access / modify: By key → dict["Hello"]
#   Change value: dict["Hello"] = "Hi"

# PRE-CHECK

# VERIFY
# - Check Python
#   python --version
#   python3 --version
#   python2 --version

# - Check flake8 / norminette
#   norminette --version
#   flake8 --version  (if alias exists)

# If Python is not installed, a good user-space installer is Miniconda.
# Example (non-sudo):
# curl -L -o ~/miniconda.sh \
#   https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# bash ~/miniconda.sh -b -p $HOME/miniconda3
# $HOME/miniconda3/bin/conda init zsh
# source ~/.zshrc
# conda create -n py310 python=3.10 -y
# conda activate py310
# python --version
# pip install --upgrade pip
# pip install flake8

# If flake8 is missing and Python exists, install locally:
# python --version
# pip install --user --upgrade pip
# pip install --user flake8
