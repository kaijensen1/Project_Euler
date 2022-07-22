# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:09:12 2021

@author: Kai
"""

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def permutation(lst):
    if len(lst) == 0:
        return[]
        
    if len(lst) ==1:
        return[lst]
    
    l = []
    
    for i in range(len(lst)):
        m = lst[i]
        
        remlst = lst[:i] + lst[i+1:]
        
        for p in permutation(remlst):
            l.append([m] + p)
            
    return l



dig_list = list('0123456789')
count = 0
for i in permutation(dig_list):
    count +=1
    if count == 1000000:
        print(i)
        break
    
print


    