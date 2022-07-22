# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:43:35 2021

@author: Kai
"""

"""
Pentagonal numbers are generated by the formula, P_n = n(3n−1)/2. The first 
ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. However, their difference, 
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P_j and P_k, for which their sum and 
difference are pentagonal and D = |P_k − P_j| is minimised; what is the value 
of D?
"""
import time
import numpy as np
start = time.time()


"""Create a list of pentagonal numbers"""
def pentagonal():
    lst = []
    for n in range(1, 5000):
        lst.append(n*(3*n - 1) / 2)
    
    return(lst)

"""Returns True if num is pentagonal and False if not."""
def is_pent(num):
    s = 24*num + 1
    s = (np.sqrt(s))
    s = (s + 1) / float(6)
    return(int(s) - s) == 0

def main():
    penta_list = pentagonal()
    combinations = []
    for j in penta_list:
        for k in penta_list:
            if j != k:
                combinations.append(j + k)
                combinations.append(abs(j - k))
                
    found = False
    i = 0
    while not found:
        n1 = combinations[i]
        n2 = combinations[i + 1]
        if is_pent(n1) and is_pent(n2):
            return(n2)
        i += 2
                
    

                   
print(main())

end = time.time()
print('Runtime = ' + str(end - start)) 

        
        
        