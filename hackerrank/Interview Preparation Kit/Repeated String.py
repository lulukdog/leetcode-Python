#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    d,m = divmod(n,len(s))
    allSum = 0
    if d>0:
        oneCount = s.count('a')
        allSum += oneCount*d
    
    allSum+= s.count('a',0,m)
    return allSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
