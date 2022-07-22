# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:11:26 2021

@author: Kai
"""

"""
Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""

def sqrsum(int):
    i = 1
    sm = 0
    while i <= int:
        sm += i
        i +=1
    return(sm**2)

def sumsqr(int):
    i = 1
    total = 0
    while i <= int:
        sqr = i **2
        total += sqr
        i +=1
    return(total)

n = 100
ans = sqrsum(n) - sumsqr(n)
print(ans)