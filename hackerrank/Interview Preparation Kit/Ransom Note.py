#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d = {}
    for w in magazine:
        if d.has_key(w):
            d[w] += 1
        else:
            d[w] = 1
    
    for w in note:
        if d.has_key(w) and d[w]>=1:
            d[w] -= 1
        else:
            print "No"
            return 
    
    print "Yes"

if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
