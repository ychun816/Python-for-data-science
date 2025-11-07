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


if __name__ == "__main__":
    main()

### NOTES ###

# | Data Type    | Syntax Example          | Ordered?  | Mutable?  | Allows Duplicates?  | How to Access / Modify                                          |
# | ------------ | ----------------------- | --------  | --------  | ------------------  | --------------------------------------------------------------- |
# | List         | `["Hello", "World!"]`   | ✅ Yes    | ✅ Yes    | ✅ Yes              | By index → `list[0]` <br> Change → `list[1] = "Hi"`             |
# | Tuple        | `("Hello", "France!")`  | ✅ Yes    | ❌ No     | ✅ Yes              | By index → `tuple[0]` <br> (cannot modify, must recreate)       |
# | Set          | `{"Hello", "Paris!"}`   | ❌ No     | ✅ Yes    | ❌ No (only unique) | Check membership → `"Hello" in set` <br> Add → `set.add("new")` |
# | Dict         | `{"Hello": "42Paris!"}` | ✅ Yes*   | ✅ Yes    | Keys ❌, Values ✅  | By key → `dict["Hello"]` <br> Change → `dict["Hello"] = "Hi"`   |

#############

### PRE-CHECK ###

## VERIFY
## verify if python installed
# python --version
# python3 --version
# python2 --version

## verify flake8(norminette)
# norminette --version
# flake8 --version (if alias exists)


## if python not installed -> install python:

# download and install Miniconda into your home
# curl -L -o ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# bash ~/miniconda.sh -b -p $HOME/miniconda3

# # initialize for zsh and reload shell
# $HOME/miniconda3/bin/conda init zsh
# source ~/.zshrc

# # create a Python 3.10 environment and activate
# conda create -n py310 python=3.10 -y
# conda activate py310

# # verify
# python --version
# pip install --upgrade pip
# pip install flake8


## if no flake8(norminette) -> install flake8(norminette):
# python --version
# pip install --upgrade pip
# pip install flake8

## verify python and install flake8
# python --version
# pip install --upgrade pip
# pip install flake8

#################