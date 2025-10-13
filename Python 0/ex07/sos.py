#!/usr/bin/env python3

# 1. create dict with morse code
# 2. import dict and filter thru arg -> transform ascii to morse code 

import sys

#library 
NESTED_MORSE = {
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ", "F": "..-. ",
    "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ",
    "S": "... ", "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ", "0": "----- ", "1": ".---- ", "2": "..--- ",
    "3": "...-- ", "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. ", " ": "/ "
}

#encoder
def encode_to_morse(text):
    """ Converts a string into Morse code using the NESTED_MORSE dictionary. """

    morse_code = "" #init a empty string
    for char in text.upper():
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse_code += NESTED_MORSE[char]
    return morse_code.strip() 



def main():
    """ Main entry point. Handles command-line arguments and prints Morse code """
    try :
        #check args
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
            # print("Wrong number of arguments")

        input_text = sys.argv[1]
        morse = encode_to_morse(input_text)
        print(morse, end="") #print outcome without newline
    except AssertionError as error:
        print(f"AssertionError: {error}")



if __name__ == "__main__":
    """ Transfrom ascii characters to morse code """
    main()
    # try:
    #     main()
    # except Exception as e:
    #     print(f"Error: {e}")


#OUTPUT
# $> python sos.py "sos" | cat -e
# ... --- ...$
# $> python sos.py 'h$llo'
# AssertionError: the arguments are bad
# $>



### NOTES ###

# morse code
# https://www.geeksforgeeks.org/python/morse-code-translator-python/?utm_source=chatgpt.com


# raise 
# -> like throw in c++ 

# .strip()
# remove trailing space


#############