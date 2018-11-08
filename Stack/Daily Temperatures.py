#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        """  正常遍历的思路
        l = []
        for v in temperatures:
            l.append([v,0])

        stack = []
        for v in l:
            stack.append(v)
            if len(stack)>1:
                index = len(stack)-2
                while index>=0:
                    stack[index][1] += 1
                    if stack[-1][0]>stack[index][0]:
                        stack.pop(index)
                        index -= 1
                        continue
                    index -= 1
        for v in stack:
            v[1] = 0

        result = []
        for v in l:
            result.append(v[1])

        return result
        """

        res = [0]*len(temperatures)
        l = []
        for i in range(0,len(temperatures)):
            while (len(l)>0 and temperatures[l[-1]]<temperatures[i]):
                nxt = l.pop()
                res[nxt] = i-nxt
            l.append(i)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))




