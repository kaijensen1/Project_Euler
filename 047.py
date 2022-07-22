# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:23:19 2021

@author: Kai
"""

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

import numpy as np


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
            
        

"""Returns the length of the set of prime divisors of num """
def seive(num):
    count = 2
    prime_divisors = set()
    stop_val = num/2
    while count <= stop_val:
        if num % count == 0 and prime_seive(count):
            prime_divisors.add(count)
        count += 1
    return(len(prime_divisors))   


def main():
    count = 644
    while True:
        if seive(count) == 4 and seive(count + 1) == 4 and seive(count + 2) == 4 and seive(count + 3) == 4:
            return count
        count += 1 
    
print(main())