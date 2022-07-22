# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:33:14 2021

@author: Kai
"""

"""
What is the smallest positive number that is evenly divisible by all of the
 numbers from 1 to 20?
"""

n = 2520

def func(j):
    i = 2
    while i <= 20:
        if j % i != 0:
            j +=1
            i = 2
            continue
        else:
            i +=1
            continue
        
    return(j)
    
    
print(func(n))