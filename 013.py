# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:49:25 2021

@author: Kai
"""

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit 
numbers.
"""

import numpy as np

txtnum = np.loadtxt('Euler013.txt')

total = str(sum(txtnum))

second = total.replace('.', '')

final = second[:10]
print(final)