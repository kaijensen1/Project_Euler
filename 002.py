# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:05:54 2021

@author: Kai
"""

"""
By considering the terms in the Fibonacci sequence whose values do not 
exceed four million, find the sum of the even-valued terms.
"""

def func(start):
    val = 0
    n1 = 1
    n2 = start
    while n1 < 4000001:
        if n2 % 2 ==0:
            val += n2
            
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return(val)

twoith = 2
print(func(twoith))