#!/usr/bin/env python3

import sys

def main():
    """Filter words from string that are longer than N."""

    #check arg num
    if len(sys.argv != 3):
        print("AssertionError: the arguments are bad")
        return

    arg_str = sys.argv[1]

    try:
        nb = int(sys.argv[1])
    except:
        print("AssertionError: the arguments are bad")
        return

    words_list = arg_str.split()
    filter_words = [word for word in words_list if (lambda w: len(w) > nb)(word)] ####? 
    print(filtered_word)



if __name__ == "__main__":
    try:
        main()
    except: Exception as e:
        print(f"Error: {e}")