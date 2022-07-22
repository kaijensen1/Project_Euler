# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:10:58 2021

@author: Kai
"""

"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
number is the first example having seven primes among the ten generated 
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 
56993. Consequently 56003, being the first member of this family, is the 
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not 
necessarily adjacent digits) with the same digit, is part of an eight prime 
value family.
"""

import time
from itertools import permutations
import numpy as np

start = time.time()


"""Takes in a number and returns False if negative, True if prime, and False 
    if not prime"""
def is_prime(num):
    num = int(num)
    if num < 0:
        return(False)
    stop_val = np.sqrt(num)
    count = 2
    while count <= stop_val:
        if num % count == 0:
            return(False)
        count += 1
    return(True)




def gen_family(s):
    
    for i in range(10):
        yield s.replace('*', str(i))
        
        
PRIME_FAMILY_COUNT = 8
digits = 4
done = False

while not done:
    tried_list = []
    for x in [i for i in  permutations('0123456789' + ('*' * (digits - 3)), digits) if i[0] != '0' and '*' in i]:

        initial_family = ''.join(x)
        if initial_family in tried_list:
            continue
        else:
            tried_list.append(initial_family)
            family = gen_family(initial_family)
            prime_family = [i for i in family if is_prime(i)]
        
            if len(prime_family) == PRIME_FAMILY_COUNT:
                print('digits: ' + str(digits))
                print('initial_family: ' + str(initial_family))
                print(prime_family)
                print( min(prime_family))
                #done = True
            
    end = time.time()
    print('Runtime = ' + str(end - start))     
    digits += 1
    print(digits)
    
