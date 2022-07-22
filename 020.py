# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:25:02 2021

@author: Kai
"""

"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math

x = str(math.factorial(100))

n = 1

lst = [x[i:i+n] for i in range(0, len(x), n)]

lst = list(map(int, lst))
sm = sum(lst)

print(sm)