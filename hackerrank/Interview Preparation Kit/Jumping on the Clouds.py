#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    nowIndex = 0
    jumpNum = 0
    while nowIndex<n-1:
        if nowIndex+2<n and c[nowIndex+2]==0:
            nowIndex+=2
        else:
            nowIndex+=1
        jumpNum+=1

    return jumpNum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
