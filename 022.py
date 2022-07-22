# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:27:42 2021

@author: Kai
"""

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical 
order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would 
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 
        'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 
        'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

euler022 = open('Euler022.txt', 'r')

content = euler022.read()

name_list = content.split('","')
euler022.close()

name_list[0] = name_list[0].replace('"', '')
name_list[-1] = name_list[-1].replace('"', '')
name_list.sort()

total = 0
for i in range(1,(len(name_list) + 1)):
    elem = name_list[i-1]
    sub_total = 0
    nameposish = (i)
    for i in elem:
        sub_total += dict[i]
    total += sub_total * nameposish
    
print(total)
    