import sys

__author__ = "Gustav Elmqvist"

"""
    This program prints the K_i:th valid upside down number.

    There are only seven digits that are valid upside down, and in order
    they are 0125986. Therefore we can treat K_i as a 7-base number and
    convert the 7-base number to a valid upside down number, one digit
    at a time.
"""

for K_i in map(int,sys.stdin):
    result = ""

    # Go through every digit in the K_i 7-base number and add the 
    # corresponding upside-down digit to the result
    while K_i:
        result += "0125986"[K_i%7]
        K_i //= 7

    print(result)