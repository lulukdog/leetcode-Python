#!/bin/python

import math
import os
import random
import re
import sys
import time

# Complete the time_delta function below.
def time_delta(t1, t2):
    time1 = t1[:-6]
    time2 = t2[:-6]
    s1 = time.mktime(time.strptime(time1,"%a %d %b %Y %H:%M:%S"))
    s2 = time.mktime(time.strptime(time2,"%a %d %b %Y %H:%M:%S"))
    zm1 = int(t1[-5:-4]+t1[-2:])
    zm2 = int(t2[-5:-4]+t2[-2:])
    dms = -(zm1-zm2)*60
    dhs = -(int(t1[-5:-2])-int(t2[-5:-2]))*3600

    return str(int(abs(s1 - s2 + dms+ dhs)))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        t1 = raw_input()

        t2 = raw_input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
