# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:15:50 2021

@author: Kai
"""

"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up 
of each of the digits 0 to 9 in some order, but it also has a rather 
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note 
the following:

d_2d_3d_4=406 is divisible by 2
d_3d_4d_5=063 is divisible by 3
d_4d_5d_6=635 is divisible by 5
d_5d_6d_7=357 is divisible by 7
d_6d_7d_8=572 is divisible by 11
d_7d_8d_9=728 is divisible by 13
d_8d_9d_10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations


perm = permutations([0,1,2,3,4,5,6,7,8,9])

total = 0
lst = []
for p in list(perm):
    num = int(str(p[0]) + str(p[1]) + str(p[2]) + str(p[3]) + str(p[4]) + str(p[5]) + str(p[6]) + str(p[7]) + str(p[8]) + str(p[9]))
    num_234 = int(str(p[1]) + str(p[2]) + str(p[3]))
    if p[0] == 0:
        continue

    if num_234 % 2 == 0:
        num_345 = int(str(p[2]) + str(p[3]) + str(p[4]))
        
        if num_345 % 3 == 0:
            num_456 = int(str(p[3]) + str(p[4]) + str(p[5]))
            
            if num_456 % 5 == 0:
                num_567 = int(str(p[4]) + str(p[5]) + str(p[6]))
                
                if num_567 % 7 == 0:
                    num_678 = int(str(p[5]) + str(p[6]) + str(p[7]))
                    
                    if num_678 % 11 == 0:
                        num_789 = int(str(p[6]) + str(p[7]) + str(p[8]))
                        
                        if num_789 % 13 == 0:
                            num_8910 = int(str(p[7]) + str(p[8]) + str(p[9]))
                                
                            if num_8910 % 17 == 0: 
                                total += num
                                lst.append(num)
                                
print(lst)
print(total)
print(sum(lst))