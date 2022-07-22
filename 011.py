# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:18:30 2021

@author: Kai
"""

"""
What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20×20 grid?
"""

import numpy as np

txtmatr = np.loadtxt('Euler011.txt')

#mult all sets of 4 numbers adjacent horizontally
def horiz():
    list1 = []
    i = 0
    while i < 17:
        j = 0
        while j < 17:
            x = txtmatr[i,j]*txtmatr[i,j+1]*txtmatr[i,j+2]*txtmatr[i,j+3]
            list1.append(x)
            j +=1
        i+=1
    return(max(list1))        

#mult all sets of 4 numbers adjacent vertically
def vert():
    list1 = []
    i = 0
    while i < 17:
        j = 0
        while j < 17:
            x = txtmatr[i,j]*txtmatr[i+1,j]*txtmatr[i+2,j]*txtmatr[i+3,j]
            list1.append(x)
            j +=1
        i+=1
    return(max(list1))

#mult all sets of 4 numbers adjacent diag down and to the right
def diagdright():
    list1 = []
    i = 0
    while i < 17:
        j = 0
        while j < 17:
            x = txtmatr[i,j]*txtmatr[i+1,j+1]*txtmatr[i+2,j+2]*txtmatr[i+3,j+3]
            list1.append(x)
            j +=1
        i+=1
    return(max(list1))

#mult all sets of 4 numbers adjacent diag down and to the left
def diagdleft():
    list1 = []
    i = 0
    while i < 17:
        j = 0
        while j < 17:
            x = txtmatr[i+3,j]*txtmatr[i+2,j+1]*txtmatr[i+1,j+2]*txtmatr[i,j+3]
            list1.append(x)
            j +=1
        i+=1
    return(max(list1))

listmax = []
listmax.append(horiz())
listmax.append(vert())
listmax.append(diagdright())
listmax.append(diagdleft())
print(max(listmax))