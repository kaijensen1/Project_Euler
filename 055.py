# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 09:57:32 2021

@author: Kai
"""

"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, 
never produce a palindrome. A number that never forms a palindrome through the 
reverse and add process is called a Lychrel number. Due to the theoretical 
nature of these numbers, and for the purpose of this problem, we shall assume 
that a number is Lychrel until proven otherwise. In addition you are given 
that for every number below ten-thousand, it will either (i) become a 
palindrome in less than fifty iterations, or, (ii) no one, with all the 
computing power that exists, has managed so far to map it to a palindrome. In 
fact, 10677 is the first number to be shown to require over fifty iterations 
before producing a palindrome: 4668731596684224866951378664 (53 iterations, 
28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel 
numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the 
theoretical nature of Lychrel numbers.
"""


def is_palindrome(num):
    list1 = []
    list1.extend(str(num))
    list2 = list1.copy()
    list2.reverse()
    if list2[0] == 0:
        return(False)
    elif list1 == list2:
        return(True)
    else:
        return(False)
    
    
def mult_and_add_count(num, count):
    list1 = []
    list1.extend(str(num))
    list1.reverse()
    num_rev = ''
    for i in list1:
        num_rev = num_rev + i
        
    next_val = num + int(num_rev)
    count +=1
    return(next_val, count)

def is_lychrel(num, count):
    if count > 50: 
        return(True)
    else:
        num, count = mult_and_add_count(num, count)
        
        if is_palindrome(num):
            return(False)
        else:
            isit = is_lychrel(num, count)
            if isit:
                return(True)
            else:
                return(False)
            
        
        

def main():
    num_lychrel = 0
    for i in range(1,10001):
        isit = is_lychrel(i,0)
        if isit:
            num_lychrel += 1
            
    return(num_lychrel)
        
    
    

if __name__ == '__main__':
    print(main())
