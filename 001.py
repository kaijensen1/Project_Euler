# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:36:24 2021

@author: Kai
"""

"""Find the sum of all the multiples of 3 or 5 below 1000."""


def func(num):
    num +=1
    val = 0
    while num < 1000:
        if num % 3 == 0 and num % 5 == 0:
            val += num
        elif num % 3 == 0:
            val += num
        elif num % 5 ==0:
            val += num
        num += 1
    return(val)


num = 0
print(func(num))