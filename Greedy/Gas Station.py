#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
       
      	minusL = []
      	for i in range(len(gas)):
      		minusL.append(gas[i]-cost[i])

      	start,preSum,tempSum = -1,0,0
      	for i in range(len(minusL)):
      		if minusL[i]>0 and start==-1:
      			print(i,start)
      			start = i
      		tempSum += minusL[i]
      		if tempSum<0:
      			preSum += tempSum
      			tempSum = 0
      			start = -1

      	if tempSum+preSum>=0:
      		return start if start>=0 else 0
      	else:
      		return -1



if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit([2],[2]))






