# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:10:30 2021

@author: Kai
"""

"""
An irrational decimal fraction is created by concatenating the positive 
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the n^th digit of the fractional part, find the value of the 
following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

subscripts = [1,10,100,1000,10000,100000,1000000]


"""create list of digits of this irrational decimal fraction """
def decimal_list(stop_val):
    full_list = []
    count = 0
    while len(full_list) < stop_val + 1:
        full_list.extend(str(count))
        count += 1
    return(full_list)


""" """
def main(subscripts):
    full_list = decimal_list(max(subscripts))
    total_prod = 1
    for n in subscripts:
        total_prod *= int(full_list[n])
        
    return(total_prod)

print(main(subscripts))

