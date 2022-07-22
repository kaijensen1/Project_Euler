# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:06:14 2021

@author: Kai
"""

"""
The fraction 49/98 is a curious fraction, as an inexperienced 
mathematician in attempting to simplify it may incorrectly believe 
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator 
and denominator.

If the product of these four fractions is given in its lowest common 
terms, find the value of the denominator.
"""
import numpy as np
from fractions import Fraction

lst = []
for p in range(10,100):
    for q in range(10,100):
        reduced = p / q
        if reduced >= 1.0:
            continue
        
        p_str = str(p)
        q_str = str(q)
        
        for l in p_str:
            if l in q_str:
                rp_str = p_str.replace(l,'')
                rq_str = q_str.replace(l, '')
                if not len(rp_str) or not len(rq_str) or int(rq_str) ==0:
                    continue
                if  int(rp_str) / int(rq_str) == reduced and p%10 != 0:
                    lst.append(Fraction(int(rp_str),int(rq_str)))
                    
print(lst)
print(np.prod(lst))
                    
                
                
