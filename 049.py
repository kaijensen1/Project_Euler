# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:03:30 2021

@author: Kai
"""

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
increases by 3330, is unusual in two ways: (i) each of the three terms are 
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?
"""

""" 1) cycle through all numbers between 1000 and 10000
    2) check if its prime
    4) create list of permutations of the digits
    5) create list of permutations that are also prime
    6) if length of the list is 3, sort and find differences
"""

import numpy as np
from itertools import permutations
from itertools import combinations


"""Takes in a number and returns True if prime, and False if not prime"""
def seive(num):
    stop_val = np.sqrt(num)
    count = 2
    while count <= stop_val:
        if num % count == 0:
            return(False)
        count += 1
    return(True)

"""takes in a prime number, creates a permutation object with its digits.
and returns a list of these permutations that is prime. """
def prime_permutations(num):
    perm = permutations(str(num))
    prime_list = []
    for i in perm:
        if i[0] == '0':
            continue
        elem = ''
        for digit in i:
            elem = elem + digit
        if seive(int(elem)) and int(elem) not in prime_list:
            prime_list.append(int(elem))
            
    return(prime_list)


def main():
    master_list = []
    for j in range(1000,10000):
        if seive(j):
            prime_list = prime_permutations(j)
            if len(prime_list) >= 3:
                prime_list.sort()
                comb = combinations(prime_list, r = 3)
                for k in comb:
                    if k[0] - k[1] == k[1] - k[2]:
                        if k not in master_list:
                            master_list.append(k)
    
    return(master_list)

print(main())
        
    