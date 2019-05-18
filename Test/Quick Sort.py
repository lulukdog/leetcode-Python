
#!/bin/python

import math
import os
import random
import re
import sys

def quickSort(l,begin,end):
	if begin>=end: return

	left = begin
	right = end
	mid = l[begin]
	while left<right:
		while l[right]>=mid and left<right:
			right -= 1
		while l[left]<=mid and left<right:
			left+=1
		l[left],l[right] = l[right],l[left]

		print (1,l)

	l[begin],l[left] = l[left],l[begin]

	print (2,l)

	# print (l,left,right)

	quickSort(l,begin,left-1)
	quickSort(l,left+1,end)


if __name__ == '__main__':
	l = [23,22,2,14,3,324]
   	quickSort(l,0,5)
   	print l
