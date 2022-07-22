# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:22:28 2021

@author: Kai
"""

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

x = str(2**1000)


n = 1

lst = [x[i:i+n] for i in range(0, len(x), n)]

lst = list(map(int, lst))
sm = sum(lst)

print(sm)