"""
https://codelearn.io/training/detail/326337
see details in electronicScreen.png
"""

from textwrap import wrap

def electronicScreen(s):
    split_str = wrap(s, 8)      # split the string into chunks of 8 characters and put them into a list
    digits = ''                 # empty string which will contain the final number

    for i in split_str:
        if i == '01011111':
            digits += '0'
        elif i == '00000101':
            digits += '1'
        elif i == '01110110':
            digits += '2'
        elif i == '01110101':
            digits += '3'
        elif i == '00101101':
            digits += '4'
        elif i == '01111001':
            digits += '5'
        elif i == '01111011':
            digits += '6' 
        elif i == '01000101':
            digits += '7'
        elif i == '01111111':
            digits += '8'
        elif i == '01111101':
            digits += '9'
        
    return digits
