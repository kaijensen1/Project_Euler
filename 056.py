# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:03:44 2021

@author: Kai
"""

"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the 
maximum digital sum?
"""

best = 100
for a in range(1,100):
    for b in range(1,100):
        test = a**b
        
        test_list = []
        test_list.extend(str(test))
        test_list = [int(i) for i in test_list]
        test_sum = sum(test_list)
        
        if test_sum > best:
            best = test_sum
            
print(best)