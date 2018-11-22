#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        queue = []
        def push(i,j):
            if i<len(nums1) and j<len(nums2):
                heapq.heappush(queue,[nums1[i]+nums2[j],i,j])

        res = []
        push(0,0)
        while queue and len(res)<k:
            _,i,j = heapq.heappop(queue)
            push(i,j+1)
            res.append([nums1[i],nums2[j]])
            if j==0:
                push(i+1,0)

        return res
        


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs([1,4,11],[2,4,6],3))




