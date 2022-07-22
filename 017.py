# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:34:26 2021

@author: Kai
"""

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with 
British usage.
"""
import re



# creates list of integers from 1 - 1000
nums = []
i = 1
while i <= 1000:
    nums.append(i)
    i +=1
    
# conversts integers to strings
numstr = []
for i in nums:
    numstr.append(str(nums[i-1]))
    
    

        
"""counting 1's digit when not in teens"""
def onedigit(elem):
    #one, two, six
    if elem == '1' or elem == '2' or elem == '6':
        return 3
    #three, seven, eight
    elif elem == '3' or elem == '7' or elem == '8':
        return 5
    #four, five, nine
    elif elem == '4' or elem == '5' or elem == '9':
        return 4
    else:
        return 0

"""counting tens and ones digit when then are between 10 - 19 """
def teens(ones):
    #ten
    if ones =='0':
        return 3
    #eleven, twelve
    elif ones =='1' or ones =='2':
        return 6
    #thirteen, fourteen, eighteen, nineteen
    elif ones =='3' or ones =='4' or ones =='8' or ones =='9':
        return 8
    #fifteen, sixteen
    elif ones =='5' or ones =='6':
        return 7
    #seventeen
    elif ones =='7':
        return 9


"""counting tens digit when not in teens"""
def twenty_up(tens):
    #twenty, thirty, eighty, ninety
    if tens == '2' or tens == '3' or tens == '8' or tens == '9':
        return 6
    #fifty, sixty, forty
    elif tens == '5' or tens == '6' or tens == '4':
        return 5
    #seventy
    elif tens == '7':
        return 7
    else:
        return 0

"""funtion that counts letters for 10 - 99"""
def twodigit(elem):
    twodigRegex = re.compile(r'^(\d)(\d)$')
    mo = twodigRegex.search(elem)
    #10 - 19
    if mo.group(1) == '1':
        return teens(mo.group(2))
    #20 - 99
    else:
        return (twenty_up(mo.group(1)) + onedigit(mo.group(2)))


"""funtion that counts letters for 100 - 999"""
def threedigit(elem):
    threedigRegex = re.compile(r'^(\d)(\d)(\d)$')
    mo = threedigRegex.search(elem)
    if mo.group(2) == '0' and mo.group(3) == '0':
        localtot = 7
    else:
        localtot = 10
    localtot += onedigit(mo.group(1))
    localtot += twodigit(mo.group(2) + mo.group(3))
    return localtot
    


total = 0
for i in numstr:
    
    if len(i) ==1:
        single = onedigit(i)
        total += single
    elif len(i) ==2:
        double = twodigit(i)
        total += double


    elif len(i) == 3:
        triple = threedigit(i)
        total += triple
    else:
        total += 11

print (total)



