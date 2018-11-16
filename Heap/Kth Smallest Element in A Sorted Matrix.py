#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = []
        for v in matrix:
            l += v
        l.sort()
        return l[k-1]


if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest([[ 1,  5,  9], [10, 11, 13], [12, 13, 15]],8))




