# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:20:28 2021

@author: Kai
"""

"""
Surprisingly there are only three numbers that can be written as the sum 
of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth 
powers of their digits.
"""

def digit_powersum(num_str):
    total = 0
    for j in num_str:
        total += int(j)**5
    return(total)

list = []
for i in range(33,1000000):
    dpsum = digit_powersum(str(i))
    if dpsum == i:
        list.append(i)
        
print(sum(list))