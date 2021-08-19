#!/usr/bin/env python
# coding: utf-8

import sys

date_temp = {} 

for line in sys.stdin:
    
    #parse the string together using strip and split 
    line = line.strip()
    
    date, temp = line.split('\t')
    
    #Used to remove any missing values for dry bulb temp which appear as ('-')
    try:
        int(temp)
    except ValueError:
        continue
    
    #store date and temperature in dictionary, to easily access items(temperatures) associated with each key(date)
    if date in date_temp:
        date_temp[date].append(int(temp))
        
    else:
        date_temp[date] = []
        date_temp[date].append(int(temp))


date_min_max = {}
print('%s  \t    %s' % ('Date', 'Min and Max Dry Bulb Temp'))

#Use all items(temperatures) associated with each key(date) to find min and max   
for date in date_temp.keys():
    date_min_max[date] = sorted(date_temp[date])[0], sorted(date_temp[date])[-1]
    
    print ('%s\t%s' % (date , date_min_max[date]))

