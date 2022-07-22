# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:47:53 2021

@author: Kai
"""

"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


"""Function that takes in num and total and and adds num^num to the total """
def sequence(num, total):
    value_added = num**num
    if len(str(value_added)) > 14:
        value_added = int(str(value_added)[-12:])
    total += value_added
    return(total)
    

def main():
    total = 1
    for count in range(2,1000):
        total = sequence(count, total)
        if len(str(total)) >= 14:
            total = int(str(total)[-12:])
    total = str(total)[-10:]
    return(total)


print(main())
            
    