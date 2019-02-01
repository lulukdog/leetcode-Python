#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

# Definition for singly-linked list.
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        res = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i]>=(i+1):
                res = i+1

        return res

        


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([100]))




