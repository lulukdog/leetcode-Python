#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
from heapq import *

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for v in s:
            if dic.has_key(v):
                dic[v] += 1
            else:
                dic[v] = 1
        tmp = sorted([i for i in s], key = lambda x: dic[x], reverse=True)
        return ''.join(tmp)


if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort('tree'))




