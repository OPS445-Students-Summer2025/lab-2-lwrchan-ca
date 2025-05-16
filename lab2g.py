#!/usr/bin/env python3
#Author: Leung Wai Rene Chan
#Author ID: 160682231
#Date Created: 2025/05/16

import sys

#check if a argument was entered, if argument was entered, assign to timer, if no argument was entered, timer=3
if len(sys.argv) >1:
    timer = int(sys.argv[1])
else:
    timer = 3


while timer != 0:
    print(timer)
    timer = timer -1
print('blast off!')



