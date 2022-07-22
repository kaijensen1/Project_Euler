# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:32:42 2021

@author: Kai
"""

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10,000.
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


total = []
for i in range(4,10001):
    i_div_sum = seive(i)
    j_div_sum = seive(i_div_sum)
    if i == j_div_sum and i != i_div_sum:
        total.append(i)

print(total)
print(sum(total))