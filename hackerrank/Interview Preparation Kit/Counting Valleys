#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleyCount = 0
    nowLevel = 0
    upLevel = False
    for i in range(n):
        if s[i]=='D':
            nowLevel -= 1
        else:
            nowLevel += 1
        
        if nowLevel>=0 and not upLevel:
            upLevel = True

        if nowLevel<0 and upLevel:
            upLevel = False
            valleyCount += 1
    
    if s[0] == 'D':
        valleyCount += 1
    
    return valleyCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
