"""
https://codelearn.io/training/detail/326337
see details in electronicScreen.png
"""

from textwrap import wrap

def electronicScreen(s):
    split_str = wrap(s, 8)      # split the string into chunks of 8 characters and put them into a list
    digits = ''                 # empty string which will contain the final number

    for i in split_str:
        match i:
            case '01011111':
                digits + '0'
            case '00000101':
                digits + '1'
            case '01110110':
                digits + '2'
            case '01110101'):
                digits + '3'
            case '00101101':
                digits + '4'
            case '01111001':
                digits + '5'
            case '01111011':
                digits + '6' 
            case '01000101':
                digits + '7'
            case '01111111':
                digits + '8'
            case '01111101':
                digits + '9'
        
    return digits
