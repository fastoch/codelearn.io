def count_bits_prime(L,R):
    myList = []         
    count_bit_1 = 0         # keeps track of the number of bits set to 1 for each integer between L and R
    is_prime = False        # check for each number if its corresponding count_bit_1 is True
    count_is_prime = 0      # counts how many binary numbers between L and R have a count_bit_1 that is prime

    for number in range(L, R+1):
        conv = str(bin(number))              # convert numbers into binaries and binaries into strings
        myList = myList.append(conv)         # Then, feed my list with those strings 
                                                
        for item in myList:                 # for each string/binary in myList
            for i in range(0, len(i)):      # check every single character
                if myList[i] == "1":        # if it's a 1
                    count_bit_1 += 1        # increment count_bit_1

            # checking if current count_bit_1 is prime 
            for n in range(2, count_bit_1):
                if (count_bit_1 % n) == 0:      
                    is_prime = False
                else 
                    is_prime = True             

            count_bit_1 = 0             # reset count_bit_1 for checking next item in my list 

    return count_is_prime
