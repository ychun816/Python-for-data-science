#!/usr/bin/env python3

# no code in global scope

import sys


def main():
    """Analyze the text provided as argument or user input."""

    # check args nb
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("Give me the text to count?\n")
        # print(text)

    # init
    upper = 0
    lower = 0
    punct = 0
    space = 0
    digit = 0

    # for loop
    for letter in text:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
        elif letter.isdigit():
            digit += 1
        elif letter.isspace():
            space += 1
        else:
            punct += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")

# test
# "Hello World! 42"

# OUTPUT
# Example invocation (truncated to fit 79 chars):
# $> python building.py "Python 3.0, released in 2008, was a major
# revision that is not completely backward-compatible with earlier
# versions. Python 2 was discontinued with version 2.7.18 in 2020."
#
# The text contains 171 characters:
# 2 upper letters
# 121 lower letters
# 8 punctuation marks
# 25 spaces
# 15 digits
# $>

# RULES
# Any exception not caught will invalidate the exercises.
# -> handle all errors using try/except.

# In Python, every function should have a docstring (a short description
# inside triple quotes).

# pip install flake8
# alias norminette=flake8
# run norminette [.py]

# NOTES
# triple quotes -> official documentation strings (docstrings) ->
# function's or module's description

# sys.argv : list of command-line arguments
# len() : length of list or string
# input() : gets user input
# f-string : fast and readable string formatting
# try/except : safe error handling
# if __name__ == "__main__" : script entry point

# def main():
#     ...
# if __name__ == "__main__":
#     main()
# -> telling Python: "This file can run independently (standalone), not
# just be imported by another script."
