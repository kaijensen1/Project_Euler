# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 09:31:26 2021

@author: Kai
"""

"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 
.

In general, 
 
, where , , and .

It is not until , that a value exceeds one-million: 
.

How many, not necessarily distinct, values of 
 for , are greater than one-million?
"""
import math

count = 0
for n in range(1,101):
    for r in range(2,n + 1):
        num_comb = (math.factorial(n))/(math.factorial(r) * math.factorial(n - r))
        if num_comb > 1000000:
            count += 1
            
print(count)