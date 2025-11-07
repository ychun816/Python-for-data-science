#!/usr/bin/env python3

# 1. create dict with morse code
# 2. import dict and filter thru arg -> transform ascii to morse code

import sys

# The morse map was previously a module-level variable; move it inside the
# encoder to avoid module-level globals (exercise rule).


def encode_to_morse(text):
    """Convert a string into Morse code.

    The morse mapping is created inside the function to avoid
    module-level mutable globals. This keeps the module import-safe.
    """
    NESTED_MORSE = {
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        " ": "/ ",
    }

    morse_code = ""
    for char in text.upper():
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse_code += NESTED_MORSE[char]
    return morse_code.strip()


def main():
    """Main entry point.

    Handles command-line arguments and prints Morse code.
    """
    try:
        # check args
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
            # print("Wrong number of arguments")

        input_text = sys.argv[1]
        morse = encode_to_morse(input_text)
        # print outcome without newline
        print(morse, end="")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    """ Transform ascii characters to morse code """
    main()


# OUTPUT
# $> python sos.py "sos" | cat -e
# ... --- ...$
# $> python sos.py 'h$llo'
# AssertionError: the arguments are bad
# $>

# NOTES ###
# morse code
# https://www.geeksforgeeks.org/python/morse-code-translator-python/

# raise
# -> like throw in c++

# .strip()
# -> remove trailing space

# end="" means:
# "Don't add a newline after printing -> end with nothing (empty string)"
#
#############
