#!/usr/bin/python3

import calendar
import time
import datetime

file = open('time.txt','w+')

with open('time.txt', 'w') as file:

  while True:
    file.write(datetime.datetime.now().ctime())
    file.write('\n')
    time.sleep(2)
    
#file.close()
