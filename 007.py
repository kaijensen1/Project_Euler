# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:00:54 2021

@author: Kai
"""

"""
What is the 10,001st prime number?
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

""" Makes a list of a given length of prime numbers"""
def prime_list(tot_len):
    count = 2
    lst = []
    while len(lst) < tot_len:
        y_n = seive(count)
        if y_n ==True:
            lst.append(count)
            count +=1
        else:
            count +=1
    return(lst)

x = int(input('Which prime number should I find?'))
fnl_list = (prime_list(x))
print(fnl_list[-1])


        