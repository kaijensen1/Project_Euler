# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:00:27 2021

@author: Kai
"""

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We 
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
and 5, giving the pandigital, 918273645, which is the concatenated product 
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


to_be_checked = set('123456789')
product_list = [1]

"""Add consecutive numbers to product_list and plug them into ..... """
def add_integer():
    master_list = []
    for i in range(2,10):
        product_list.append(i)
        master_list.append(pandigit(product_list))
        
    return(max(master_list))



"""takes in a list of integers and adds the concatinated sum to 
master_list if it is pandigital """
def pandigit(product_list):
    current_list = []
    x = len(product_list)
    if x >= 6:
        x = 5
    for i in range(10**(5 - x),10**(6 - x)):
        digit_list = ''
        
        for j in product_list:
            digit_list = digit_list + str(j*i)
        
        if len(digit_list) != 9:
            continue
        elif set(digit_list) == to_be_checked:
            current_list.append(int(digit_list))
            
    if current_list == []:
        return(1)
    else:
        return(max(current_list))


print(add_integer())

