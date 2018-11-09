#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position)<=1:
            return len(position)

        stack = []
        for i in range(0,len(position)):
            stack.append([position[i],speed[i]])

        stack.sort(key = lambda x:x[0])
        for i in range(0,len(stack)):
            stack[i] = float((target-stack[i][0]))/stack[i][1]

        count = 1
        maxDis = stack[-1]
        for i in range(len(stack)-2,-1,-1):
            dis = stack[i]
            if dis==stack[i+1] and dis==maxDis:
                continue
            elif dis>=maxDis:
                maxDis = dis
                count+=1

        return count



if __name__ == '__main__':
    s = Solution()
    print(s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))




