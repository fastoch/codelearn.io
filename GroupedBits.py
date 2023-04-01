"""
https://codelearn.io/training/detail/40509  

Given an integer n, count the number of groups of consecutive 1 bits in its binary representation.

For n = 1259, the output should be GroupedBits(n) = 4.
The binary representation of 1259 is 10011101011, wich contains 4 groups of 1 bits.
"""

import re

def groupedBits(n):
    bin_rep = bin(n)                # binary representation of n
    str_rep = str(bin_rep)          # converting bin_rep to string type
    x = re.findall("1+", str_rep)   # findall() returns a list containing all matches
    return len(x)
