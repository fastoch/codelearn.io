def groupedBits(n):
    num_groups_1 = 0        
    bin_rep = bin(n)        # binary representation of n
    str_rep = str(bin_rep)  # converting bin_rep to string type
    for i in str_rep:
        if i == '1':
            num_groups_1 += 1
    return num_groups_1
    
# issue: counting 1 bits individually, even grouped ones
