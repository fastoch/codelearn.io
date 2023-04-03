def count_bits_prime(L,R):
    myList = []         
    count_bit_1 = 0     # keeps track of the number of bits set to 1 for each integer between L and R
    is_prime = 0        # keeps track of the number of count_bit_1 that are prime 

    for i in range(L, R+1):
        conv = str(bin(i))              # convert numbers into binaries and binaries into strings
        myList = myList.append(conv)    # Then, feed my list with those strings 
                                                
        for i in myList:                # for each string/binary in myList
            for j in range(len(i)):     # check every single character
                if myList[j] == "1":    # if it's a 1
                    count_bit_1 += 1    # increment count_bit_1
            # TODO: 
            # if count_bit_1 is prime:
            #   is_prime += 1           # increment is_prime

            count_bit_1 = 0             # reset count_bit_1

    return is_prime
