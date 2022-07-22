# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 15:32:00 2021

@author: Kai
"""
"""
opens file to read and converts each line into a list that is stored in another
 list
"""
euler018 = open('Euler018.txt', 'r')
list_of_lists = []
for line in euler018:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)
euler018.close()

"""converts all values in list_of_lists from strings to integers """
list_of_lists = [[int(float(j)) for j in i] for i in list_of_lists]




while len(list_of_lists) != 1:
    for i in range(len(list_of_lists[-2])):
        list_of_lists[-2][i] = list_of_lists[-2][i] + max(list_of_lists[-1][i], list_of_lists[-1][i+1])
    list_of_lists.pop(-1)       #removes the last list from list of lists
    for i in list_of_lists:
        print(i)
        