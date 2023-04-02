"""
https://codelearn.io/training/detail/326337
see details in electronicScreen.png
"""

from textwrap import wrap

def electronicScreen(s):
    split_str = wrap(s, 8)      # splitting the string into chunks of 8 characters
    digits = ""                 # empty string which will contain the final number

    for i in split_str:
        match split_str:
            case'01011111':
                digits + 0
            case '00000101':
                digits + 1
            case '01110110':
                digits + 2
            case '01110101'):
                digits + 3
            case '':
                digits + 4
            case '':
                digits + 5
            case '':
                digits + 6 
            case '':
                digits + 7
            case '':
                digits + 8
            case '':
                digits + 9
        
    return 
