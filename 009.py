# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:42:51 2021

@author: Kai
"""

"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
"""




def triples(num):
    a = 1
    b = 1
    c = num - a - b
    
    while c > 1:
        if a**2 +b**2 ==c**2:
            return(a,b,c)
        
        while a < 998:
            b = 1
            c = 1000 - a - b
            while b < 1000- a - 1:
                if a**2 +b**2 ==c**2:
                    return(a*b*c)
                b += 1
                c = 1000 - a - b        
            a +=1

            
num = 1000
            
print(triples(num))
        