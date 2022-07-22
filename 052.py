# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:05:04 2021

@author: Kai
"""

"""
It can be seen that the number, 125874, and its double, 251748, contain 
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
"""

def main():
    i = 1
    while True:
        i += 1
        x6 = i * 6
        x5 = i * 5
        
        if len(str(x6)) != len(str(i)):
            continue
        elif sorted(str(x6)) == sorted(str(x5)):
            x4 = i * 4
            if sorted(str(x4)) == sorted(str(x5)):
                x3 = i * 3
                if sorted(str(x3)) == sorted(str(x4)):
                    x2 = i * 2
                    if sorted(str(x2)) == sorted(str(x3)):
                        print(i)
                        break
        
        
        
if __name__ == '__main__':
    print(main())
            