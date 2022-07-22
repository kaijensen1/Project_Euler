# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:46:40 2021

@author: Kai
"""

"""
If p is the perimeter of a right angle triangle with integer length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math

master_dict = {}
for p in range(12,1001):

    
    counter = 0
    for c in range(math.ceil(p/2),math.floor(p/3), -1):
        for b in range(1,c - 1):
            a = p - c - b
            if a <= 0 or a >= c:
                continue
            elif a**2 + b**2 == c**2:
                counter +=1
                break
    if counter > 0:
        master_dict[p] = counter
                
max_key = max(master_dict, key = master_dict.get)  
print(max_key)   