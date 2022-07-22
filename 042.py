# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 12:32:18 2021

@author: Kai
"""

"""
The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. For 
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value 
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle 
words?
"""

dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 
        'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 
        'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

euler042 = open('Euler042.txt', 'r')

content = euler042.read()

word_list = content.split('","')
euler042.close()


word_list[0] = word_list[0].replace('"', '')
word_list[-1] = word_list[-1].replace('"', '')

"""
Creates a list of triangle numbers.
"""
triangle_list = []

for n in range(1,40):
    triangle_list.append( .5*n*(n+1))



total = 0
triangle_words = []
for i in range((len(word_list))):
    elem = word_list[i]
    sub_total = 0
    for i in elem:
        sub_total += dict[i]
        
    if sub_total in triangle_list:
        total += 1
        triangle_words.append(elem)
      
print(triangle_words)
print(total)

        
    
    
