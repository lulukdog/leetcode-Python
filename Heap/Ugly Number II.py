#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [1]
        index2,index3,index5 = 0,0,0
        min2,min3,min5 = 2,3,5
        while len(l)<n:
            while min2<=l[-1]:
                min2 = l[index2]*2
                index2 += 1
            while min3<=l[-1]:
                min3 = l[index3]*3
                index3 += 1
            while min5<=l[-1]:
                min5 = l[index5]*5
                index5 += 1
            l.append(min(min2,min3,min5))

        return l[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))




