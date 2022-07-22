# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:28:02 2021

@author: Kai
"""

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


nums = []
i = 1
while i < 1000000:
    nums.append(i)
    i +=1
    
nums.sort(reverse = True)

bestlist = []

for j in nums:
    newlist = [j]
    while j != 1:
        
        if j % 2 ==0:
            j = j/2
            newlist.append(int(j))
        else:
            j = 3*j + 1
            newlist.append(int(j))
    
    if len(newlist) > len(bestlist):
        bestlist = newlist
        
print(bestlist)