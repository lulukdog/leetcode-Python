#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        startIndex = 0
        for i in range(0,len(asteroids)):
            stack.append(asteroids[i])
            startIndex = i
            if asteroids[i]>0:
                break

        for i in range(startIndex+1,len(asteroids)):
            if asteroids[i]<0:
                j = len(stack)-1
                needAddList = False
                if j<0:
                    stack.append(asteroids[i])
                while j>=0:
                    if stack[j]<0:
                        stack.append(asteroids[i])
                        needAddList = False
                        break
                    else:
                        if asteroids[i]+stack[j]<0:
                            j-=1
                            stack.pop()
                            needAddList = True
                        elif asteroids[i]+stack[j]==0:
                            j-=1
                            stack.pop()
                            needAddList = False
                            break
                        else:
                            needAddList = False
                            break
                if needAddList:
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])

        return stack

            

        

if __name__ == '__main__':
    s = Solution()
    print(s.asteroidCollision([1,-1,-2,-2]))




