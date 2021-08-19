#!/usr/bin/env python
# coding: utf-8

import sys

date_temp = {} 

for line in sys.stdin:
    
    #parse the string together using strip and split 
    line = line.strip()
    date, temp = line.split('\t')
    
    #Used to remove any values temperatures with dashes('-')
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
        
date_stdev = {}

print('%s  \t        %s' % ('Date', 'Stdev'))

#Use all items(temperatures) associated with each key(date) to calculate stdev   
for date in date_temp.keys():
    
    #setting variables for stdev formula
    
    x_i = date_temp[date]
    N = len(x_i)
    mean = sum(x_i)/N
    x_i_manipulated = [i**2 for i in x_i]
    
    #calculating stdev
    stdev = ((sum(x_i_manipulated)-(N*mean**2))/N)**0.5
    
    date_stdev[date] = stdev
    
    print ('%s\t%s' % (date,date_stdev[date]))


    