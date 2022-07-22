# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:20:59 2021

@author: Kai
"""

"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)
"""

""" Returns True if number passed to it is a palindrome """

def palindromes(num):
    list1 = []
    list1.extend(str(num))
    list2 = list1.copy()
    list2.reverse()
    if list1 == list2:
        return(True)
    else:
        return(False)


"""converts a base 10 number to base 2 """
def switch_base(base_ten):
    str_base_two = ''
    powers_of_two = [2**i for i in range(19,-1,-1)]
    for j in powers_of_two:
        if base_ten >= j:
            base_ten -= j
            str_base_two = str_base_two + '1'
        else:
            str_base_two = str_base_two + '0'
    return(int(str_base_two))
        
    
def main(stop_val):
    pals = []
    for i in range(1,stop_val):
        if palindromes(i) == True:
            base_two = switch_base(i)
            if palindromes(base_two) == True:
                pals.append(i)
    return(pals)

print(sum(main(1000000)))