# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:51:31 2021

@author: Kai
"""

"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""

i = 999


def func(i):
    pals = []
    while i > 99:
        j = i
        while j > 99:
            val = i*j
            list1 = []
            list1.extend(str(val))
            list2 = list1.copy()
            list2.reverse()
            if list1 == list2:
                pals.append(val)
            j -=1
        i -=1
    pals.sort()
    return(pals[-1])

print(func(i))
        
