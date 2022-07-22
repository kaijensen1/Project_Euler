# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 10:15:58 2021

@author: Kai
"""

"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import numpy as np


"""Takes in a number and returns True if prime, and False if not prime"""
def seive(num):
    stop_val = np.sqrt(num)
    count = 2
    while count <= stop_val:
        if num % count == 0:
            return(False)
        count += 1
    return(True)


to_be_checked = set('123456789')


""" returns True if a number is pandigital and False if it is not """
def pandigital(num):
    num_str = str(num)
    to_be_checked = set()
    
    for i in range(1,len(num_str) + 1):
        to_be_checked.add(str(i))
    
    if len(num_str) == i and set(num_str) == to_be_checked:
        return(True)
    
    
    
def main():
    for i in range(10000000, 2143, -1):
        if seive(i) == True and pandigital(i) == True:
            return(i)

print(main())