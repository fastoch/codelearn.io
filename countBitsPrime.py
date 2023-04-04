def count_bits_prime(L, R):
    myList = []             # will contain strings representing binary numbers between L and R
    count_bit_1 = 0         # counts the number of bits set to 1 for each integer between L and R
    count_is_prime = 0      # counts how many binary numbers between L and R have a count_bit_1 that is prime  

    for number in range(L, R+1):
        conv = str(bin(number))    # convert numbers into binaries and binaries into strings
        conv = conv[2:]            # ignore the '0b' prefix inherent to the binary conversion
        myList.append(conv)        # Then, feed my list with those strings 
                                                
    for item in myList:                     # for each string/binary in myList
        for i in range(0, len(item)):       # check every single character
            if item[i] == "1":              # if it's a 1
                count_bit_1 += 1            # increment count_bit_1

        # checking if current count_bit_1 is prime 
        if count_bit_1 > 1:                 # 0 and 1 are not prime numbers
            if count_bit_1 == 2:            # 2 is a special case since 2 % 2 == 0
                count_is_prime += 1
            elif count_bit_1 % 2 != 0:
                count_is_prime += 1

        count_bit_1 = 0        # reset count_bit_1 for checking next item in my list 

    return count_is_prime
