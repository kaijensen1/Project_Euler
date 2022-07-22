# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:44:00 2021

@author: Kai
"""

"""
It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a 
prime and twice a square?
"""

import time
import numpy as np
start = time.time()


"""Takes in a number and returns False if negative, True if prime, and False 
    if not prime"""
def prime_seive(num):
    if num < 0:
        return(False)
    stop_val = np.sqrt(num)
    count = 2
    while count <= stop_val:
        if num % count == 0:
            return(False)
        count += 1
    return(True)

"""takes in a composite integer and returns True if odd and composite and 
False if not"""
def composite_seive(num):
    if ((num - 1) / 2) % 1 == 0:
        return(True)
    return(False)
    


"""creates a set of prime numbers and odd composite numbers below a given 
value"""
def create_lists(stop_val):
    prime_list = []
    composite_list = []
    for i in range(2,stop_val):
        if prime_seive(i):
            prime_list.append(i)
            
        elif composite_seive(i):
            composite_list.append(i)
            
    return(prime_list, composite_list)
            

def main(stop_val):
    prime_list, composite_list = create_lists(stop_val)
    
    produce_integer = set()
    not_produce_integer = set()
    
    for p in prime_list:
        for c in composite_list:
            if (c - p) < 0:
                continue
            elif np.sqrt((c - p)/2) % 1 == 0:
                produce_integer.add(c)
            else:
                not_produce_integer.add(c)
                
    for i in not_produce_integer:
        if i not in produce_integer:
            return(i)
            
    return('failed to find')


print(main(100000))

end = time.time()
print('Runtime = ' + str(end - start))