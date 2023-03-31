"""
https://codelearn.io/training/detail/131003

Given two integers, l and r, find the maximal value of a xor b, where a and b satisfy the following condition:

l <= a <= b <= r 

For l=10 and r=12 the output should be maxXOR(l,r)=7

For l=11 and r=100 the output should be maxXOR(l,r)=127

"""

def maxXOR(l,r):
    list = []                       # list which will contain the results of all XOR operations
    for i in range(l, r):  
        for j in range(l+1, r+1):   
            list.append(i^j)        # add the result of each xor operation to my list
    return max(list)     
