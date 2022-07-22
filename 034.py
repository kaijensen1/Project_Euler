# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:51:03 2021

@author: Kai
"""

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial 
of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

import numpy as np

total = 0
for i in range(10,1000000):
    str_i = str(i)
    running_sum = 0
    for digit in str(i):
        running_sum += np.math.factorial(int(digit))
    if running_sum == i:
       total += i
       
print(total)