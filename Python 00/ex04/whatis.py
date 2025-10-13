
import sys
# print(sys.argv)

arg = sys.argv


if len(arg) == 1:
    exit()
elif len(arg) > 2:
    print("AssertionError: more than one argument is provided")
else: 
    try:
        nb = int(arg[1])
        if int(arg[1]) % 2 != 0:
            print("I'm Odd.")
        elif int(arg[1]) % 2 == 0:
            print("I'm Even.")
    except ValueError:
        print("AssertionError: argument is not an integer")

# return 0



## OUTPUT ##
# $> python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# AssertionError: more than one argument is provided




#### NOTES ######################

#learn to take arg 

# sys.argv is a list of strings.
# sys.argv[0] → script name (whatis.py)
# sys.argv[1] → first argument passed


################################