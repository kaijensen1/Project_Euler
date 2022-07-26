# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:23:28 2021

@author: Kai
"""

"""
You are given the following information, but you may prefer to do some research 
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.

Jan 31
Feb 28 or 29
Mar 31
Apr 30
May 31
Jun 30
Jul 31
Aug 31
Sep 30
Oct 31
Nov 30
Dec 31

How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
"""


from datetime import date
        
sunday = 6

start = date(1901, 1, 1)    
end = date(2000, 12, 31)

count = 0
year = start.year
month = start.month

while year <= end.year and month <= end.month:
    print(str(year) + '-' + str(month))
    test = date(year, month, 1)
    if  test.weekday() == sunday:
        print('found a sunday')
        count +=1
    if month == 12:
        month = 1 
        year += 1
    else:
        month += 1

print(count)

