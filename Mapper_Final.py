#!/usr/bin/env python3
# coding: utf-8

import sys
import datetime

#Skip first line of weather data containing column names
next(sys.stdin)

for line in sys.stdin:
    #parse the string together using strip and split 
    line = line.strip().split(",")
    
    #convert integers from data in datetime objects and display them as such  
    year_month_day = datetime.datetime.strptime(line[1],'%Y%m%d').date()
    
    dry_bulb_temp = line[8]
    
    #output key-value pairs 
    print ('%s\t%s' % (year_month_day, dry_bulb_temp))
