"""
https://codelearn.io/training/detail/326337
see details in electronicScreen.png
"""

from textwrap import wrap

def electronicScreen(s):
    split_str = wrap(s, 8)      # splitting the string into chunks of 8 characters
    digits = ""                 # empty string which will contain the final number

    for i in split_str:
        switch:
            case(split_str[i] == '')    # 0
            case(split_str[i] == '')    # 1
            case(split_str[i] == '')    # 2
            case(split_str[i] == '')    # 3
            case(split_str[i] == '')    # 4
            case(split_str[i] == '')    # 5
            case(split_str[i] == '')    # 6
            case(split_str[i] == '')    # 7
            case(split_str[i] == '')    # 8
            case(split_str[i] == '')    # 9
        
    return 
