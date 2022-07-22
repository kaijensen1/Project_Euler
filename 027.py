# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:51:48 2021

@author: Kai
"""

"""
Euler discovered the remarkable quadratic formula:

It turns out that the formula will produce 40 primes for the consecutive 
integer values 0 <= n <= 39. However, when n = 40, 40^2 +40 +41 is divisible 
by 41, and certainly when n = 41, 41^2 +41 +41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 
primes for the consecutive values 0<=n<=79. The product of the coefficients, 
−79 and 1601, is −126479.

Considering quadratics of the form:
    
    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value ofn
    e.g. |11| = 11 and |-4| = 4
    
Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of , 
starting with n = 0.
"""
import numpy as np


"""Takes in a number and returns False if negative, True if prime, and False 
    if not prime"""
def seive(num):
    if num < 0:
        return(False)
    stop_val = np.sqrt(num)
    count = 2
    while count <= stop_val:
        if num % count == 0:
            return(False)
        count += 1
    return(True)

"""Take in a and b determine what range of n return primes """
def quad_test(a, b):
    n = 0
    while n > -1:
        calc_num = n**2 + a*n + b
        if seive(calc_num) == True:
            n +=1
        else:
            return(n)
            


""" holds best run so far, as well its a and b, replaces these when we get a 
better run"""

def keep_best():
    longest_run = 0
    for a in range(-999,1000):
        for b in range(-1000,1001):
            current_run = quad_test(a,b)
            if current_run > longest_run:
                best_a = a
                best_b = b
                longest_run = current_run
                
    return(best_a, best_b, longest_run, best_a * best_b)
                
print(keep_best())
        