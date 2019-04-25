#!/bin/python

import math
import os
import random
import re
import sys
import time
from dateutil.parser import parse

# Complete the time_delta function below.
def time_delta(t1, t2):
    # time1 = t1[:-6]
    # time2 = t2[:-6]
    # s1 = time.mktime(time.strptime(time1,"%a %d %b %Y %H:%M:%S"))
    # s2 = time.mktime(time.strptime(time2,"%a %d %b %Y %H:%M:%S"))
    # zm1 = int(t1[-5:-4]+t1[-2:])
    # zm2 = int(t2[-5:-4]+t2[-2:])
    # dms = -(zm1-zm2)*60
    # dhs = -(int(t1[-5:-2])-int(t2[-5:-2]))*3600

    # return str(int(abs(s1 - s2 + dms+ dhs)))

    t1 = parse(t1)
    t2 = parse(t2)
    return int(abs((t1-t2).total_seconds()))
    

if __name__ == '__main__':
    delta = time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000')
    print(delta)

