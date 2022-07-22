# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:25:48 2021

@author: Kai
"""

"""
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 28 
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than 
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers is 
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum 
of two abundant numbers.
"""
import numpy as np


"""creates list of the proper divisors of numbers passed to it, and returns the 
sum of the proper divisors"""
def seive(num):
    count = 2
    divisors = [1]
    stop_val = np.sqrt(num)
    while count <= stop_val:
        if num % count == 0:
            divisors.append(count)
            if count != (num/count):
                divisors.append(num/count)
        count += 1
    return(sum(divisors))



"""creat a list of abundant numbers"""
abundant_list = []
for i in range(12,28123):
    div_sum = seive(i)
    if div_sum > i:
        abundant_list.append(i)
        


num_list = [i for i in range(28124)]


for i in abundant_list:
    for j in abundant_list:
        if i + j in num_list:
            num_list.remove(i + j)
            
print(num_list)
print(sum(num_list))






