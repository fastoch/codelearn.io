import re

def groupedBits(n):
    bin_rep = bin(n)                # binary representation of n
    str_rep = str(bin_rep)          # converting bin_rep to string type
    x = re.findall("1+", str_rep)   # findall() returns a list containing all matches
    return len(x)
