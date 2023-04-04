def count_bits_prime(L,R):
    myList = []             # will contain strings representing binary numbers between L and R
    count_bit_1 = 0         # counts the number of bits set to 1 for each integer between L and R
    remainders = 0          # keeps track of remainders for each modulo operation on count_bit_1 
    count_is_prime = 0      # counts how many binary numbers between L and R have a count_bit_1 that is prime  

    for number in range(L, R+1):
        conv = str(bin(number))    # convert numbers into binaries and binaries into strings
        conv = conv[2:]            # ignore the '0b' prefix inherent to the binary conversion
        myList.append(conv)        # Then, feed my list with those strings 
    print(myList)
                                                
    for item in myList:                     # for each string/binary in myList
        for i in range(0, len(item)):       # check every single character
            if item[i] == "1":              # if it's a 1
                count_bit_1 += 1            # increment count_bit_1
        print(count_bit_1)

        # checking if current count_bit_1 is prime 
        if count_bit_1 == 0 or count_bit_1 == 1:    # getting rid of special cases 0 and 1
            count_is_prime = 0                      # 0 and 1 have no dividers but are not considered prime numbers
        else:
            for n in range(2, count_bit_1 + 1):     # first arg is inclusive, but second arg of range is exclusive, hence the +1 
                remainders += (count_bit_1 % n)
            # incrementing counter if it's prime (if all remainders are equal to 0)
            print("Remainders:", remainders)
            if remainders == 0:
                count_is_prime += 1
                                
        count_bit_1 = 0        # reset count_bit_1 for checking next item in my list 

    return count_is_prime

print("Result: ", count_bits_prime(6,10))
