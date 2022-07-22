# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:11:14 2021

@author: Kai
"""

"""
A unit fraction contains 1 in the numerator. The decimal representation of the 
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.
"""
import time

def main():
    d = 3000
    max_cycle_len = 0
    for i in range(1,d):
        current_cycle = find_cycle_len(i)
        if current_cycle > max_cycle_len:
            max_cycle_len = current_cycle
            i_that_produced_max = i
    print(i_that_produced_max)
        
def find_cycle_len(n):
    cycle_len = 0
    list_of_remainders = []
    x = 1
    while(True):
        if x % n == 0:
            x = 0
            break
        elif x in list_of_remainders:
            break
        list_of_remainders.append(x)
        x = (x * 10) % n
            
            
        cycle_len += 1
    return(cycle_len)
            
start_time = time.time() 
main()
print('time taken was {} seconds'.format(time.time()-start_time))
    
    