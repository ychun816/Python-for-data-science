#!/usr/bin/env python3

def count_in_list(lst, item):
    """
    Counts how many times `item` appears in `lst`.
    
    Args:
        lst (list): The list to search.
        item (any): The item to count.
    
    Returns:
        int: The number of occurrences of item in the list.
    """

    return lst.count(item)



# when you type the command "pip list" and display its characteristics
# when you type "pip show -v ft_package"

#OUTPUT
# pip show -v ft_package
# $>pip show -v ft_package
# Name: ft_package
# Version: 0.0.1
# Summary: A sample test package
# Home-page: https://github.com/eagle/ft_package
# Author: eagle
# Author-email: eagle@42.fr
# License: MIT
# Location: /home/eagle/...
# Requires:
# Required-by:
# Metadata-Version: 2.1
# Installer: pip
# Classifiers:
# Entry-points:
# $>

#COMMANDS + #OUTPUT
# pip install ./dist/ft_package-0.0.1.tar.gz
# pip install ./dist/ft_package-0.0.1-py3-none-any.whl
# from ft_package import count_in_list
# print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
# print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0