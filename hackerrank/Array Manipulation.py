#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    l = [0 for i in range(n)]
    res = 0
    for tl in queries:
        l[tl[0]-1] += tl[2]
        if tl[1] < n:
            l[tl[1]] -= tl[2]
    
    sum = 0
    for i in l:
        sum += i
        if sum>res:
            res = sum

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
