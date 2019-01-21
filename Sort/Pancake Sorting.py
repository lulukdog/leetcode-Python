#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def flipList(list,num):
            for i in range(num/2):
                list[i],list[num-i-1] = list[num-i-1],list[i]


        res = []
        maxA = max(A)
        flipLen = len(A)
        while A != sorted(A):
            index = A.index(maxA)
            if index!=0:
                flipList(A,index+1)
                res.append(index+1)
            
            flipList(A,flipLen)
            res.append(flipLen)
            maxA = maxA-1
            flipLen = flipLen-1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.pancakeSort([3,2,4,1]))




