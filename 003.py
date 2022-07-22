# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:17:49 2021

@author: Kai
"""

"""
What is the largest prime factor of the number 600851475143 ?
"""
import numpy as np


def ans(num):
    prime_div = []
    divisors = seive(num)
    for i in divisors:
        sub = seive(i)
        if sub == [1]:
            prime_div.append(i)
    return(max(prime_div))
            
        


def seive(num):
    count = 1
    divisors = []
    stop_val = np.sqrt(num)
    while count < stop_val:
        if num % count == 0:
            divisors.append(count)
        count += 1
    return(divisors)        
    
    







num = 600851475143

print(ans(num))