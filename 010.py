# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:37:19 2021

@author: Kai
"""

"""
Find the sum of all the primes below two million.
"""
import numpy as np


"""Takes in a number and returns True if prime and False if not"""
def seive(num):

    stop_val = np.sqrt(num)
    count = 2
    while count <= stop_val:
        if num % count == 0:
            return(False)
        count += 1
    return(True)

""" Makes a list of all prime numbers below stop_val"""
def prime_list(stop_val):
    count = 2
    lst = []
    while count <= stop_val:
        y_n = seive(count)
        if y_n ==True:
            lst.append(count)
        count +=1
    return(lst)

print(sum(prime_list(2000000)))
