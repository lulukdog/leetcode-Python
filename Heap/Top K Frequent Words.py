#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        for v in words:
            if d.has_key(v):
                d[v] += 1
            else:
                d[v] = 1
        def sortfunc(a,b):
            if a[1]==b[1]:
                return cmp(a[0],b[0])
            else:
                return -cmp(a[1],b[1])

        d = sorted(d.items(),cmp = sortfunc)
        l = [v[0] for v in d]
        return l[0:k]
        

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],3))




