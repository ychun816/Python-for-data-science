#!/usr/bin/env python3

# use library functions to format the output
import time 
import datetime


# def main():
# Get current time in seconds since epoch
epoch = time.time()
#now = datetime.datetime.now()

#format nb
format_normal = f"{epoch:,.4f}"
format_sci = f"{epoch:.2e}"

#format date
now = datetime.datetime.now()
format_date = now.strftime("%b %d %Y")


#print
print(f"Seconds since January 1, 1970: {format_normal} or {format_sci} in scientific notation")
print(f"{format_date}")


#OUTPUT 
# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
# $>



#### NOTES ######################
# time and datetime libraries
# https://docs.python.org/3/library/time.html

# f -> stands for “formatted string literal.” -> “This string will contain expressions inside {}

# :,.4f → grouping + 4 decimals.
# :.2e → scientific notation.

# : -> is the format specifier.
# .4f → fixed-point notation with 4 digits after the decimal
# .2e → scientific (exponential) notation with 2 digits after the decimal; e.g. 1.67e+09

# strftime formatting: There are many codes (%H hour, %M minute, %S second)

################################


