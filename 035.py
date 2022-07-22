# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 15:10:07 2021

@author: Kai
"""

"""
The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 
71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import numpy as np



"""Takes in a number and returns True if prime and False if not"""
def seive(num):
    stop_val = np.sqrt(num)
    count = 2
    while count <= stop_val:
        if num % count == 0:
            return(False)
        count += 1
    return(True)


""" Makes a list of circular prime numbers below a given stop value"""
def prime_list(stop_val):
    lst = []
    for count in range(2,stop_val):
        y_n = seive(count)
        if y_n == True:
            if find_circular(count) == True:
                lst.append(count)
    return(lst)



""" Takes in a prime number and returns true if circular """

def find_circular(prime):
    list_o_digits = []
    list_o_digits.extend(str(prime))
    for i in range(0,len(str(prime)) - 1):
        k = list_o_digits[0]
        list_o_digits.pop(0)
        list_o_digits.append(k)
        num = ''
        for elem in list_o_digits:
            num = num + elem
        if seive(int(num)) == False:
            return False
    return True


    
x = prime_list(1000000)

print(x)
print(len(x))

                
                
                
                
