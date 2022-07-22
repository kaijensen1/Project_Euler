# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:10:03 2021

@author: Kai
"""

"""
Starting with the number 1 and moving to the right in a clockwise direction a 
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?
"""

count = 1

for i in range(3,1002,2):
    n = i - 1
    count += i**2 + (i**2 - n) + (i**2 - 2*n) + (i**2 - 3*n)
    
print(count)