def count_bits_prime(L,R):
    myList = []    
    count_bit_1 = 0
    is_prime = 0        

    for i in range(L, R+1):
        conv = str(bin(i))              # convert numbers into binaries and binaries into strings
        myList = myList.append(conv)    # Then, feed my list with those strings 
                                                
        for i in myList:
            if myList[i] == "1":
                count_bit_1 += 1
    
    # test if count_bit_1 is prime
    # if so, increment is_prime

    return count_is_prime
