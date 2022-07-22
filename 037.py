# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:20:26 2021

@author: Kai
"""

"""
The number 3797 has an interesting property. Being prime itself, it is 
possible to continuously remove digits from left to right, and remain prime 
at each stage: 3797, 797, 97, and 7. Similarly we can work from right to 
left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left 
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import numpy as np


"""Takes in a number and returns True if prime and False if not"""
def seive(num):
    if num == 1:
        return(False)
    stop_val = np.sqrt(num)
    count = 2
    while count <= stop_val:
        if num % count == 0:
            return(False)
        count += 1
    return(True)


""" Makes a list of truncatable prime numbers of a given length"""
def prime_list(stop_val):
    lst = []
    count = 23
    while len(lst) < stop_val:
        
        if seive(count) == True:
            
            if find_truncate_front(count) == True and find_truncate_back(count) == True:
                lst.append(count)
                
        count += 1
        
    return(lst)

"""Takes in a prime number and returns True if truncatable from the front 
and false if not"""
def find_truncate_front(prime):
    list_o_digits = []
    list_o_digits.extend(str(prime))
    
    for i in range(1,len(str(prime))):
        list_o_digits.pop(0)
        num = ''
        
        for elem in list_o_digits:
            num = num + elem
            
        if seive(int(num)) == False:
            return False
        
    return True
    
"""Takes in a prime number and returns True if truncatable from the back 
and false if not"""
def find_truncate_back(prime):
    list_o_digits = []
    list_o_digits.extend(str(prime))
    
    for i in range(1,len(str(prime))):
        list_o_digits.pop()
        num = ''
        
        for elem in list_o_digits:
            num = num + elem
            
        if seive(int(num)) == False:
            return False
        
    return True

print(sum(prime_list(11)))