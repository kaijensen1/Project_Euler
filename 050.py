# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:38:17 2021

@author: Kai
"""

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below 
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?
"""

import time
import numpy as np
start = time.time()


"""Takes in a number and returns True if prime, and False if not prime"""
def seive(num):
    stop_val = np.sqrt(num)
    count = 2
    while count <= stop_val:
        if num % count == 0:
            return(False)
        count += 1
    return(True)


"""takes in a counter, a list of primes and returns a list of primes from the 
list that are a sum of consecutive primes of length counter. """

def counter_slice(num, prime_list):
    return_list = []
    for i in range(len(prime_list) - num + 1):
        sub_list = prime_list[i:i+num]
        if sum(sub_list) < 1000000 and seive(sum(sub_list)):
            return_list.append([sum(sub_list), len(sub_list)])
            
    return(return_list)



def main():
    master_list = []
    prime_list = []
    for i in range(2,1000000):
        if seive(i):
            prime_list.append(i)
    print(len(prime_list))
    
    for counter in range(200, 2000):
        mini_list = counter_slice(counter, prime_list)
        print(str(counter) + ' Done.')
        for i in mini_list:
            
            master_list.append(i)
            
    for i in master_list:
        print(i)
        
        
        
if __name__ == '__main__':
    print(main())

end = time.time()
print('Runtime = ' + str(end - start)) 