#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length==1:
            return 0 

        for i in range(0,length-1):
            if nums[i]>nums[i+1]:
                return i

        return length-1
            

if  __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([]))
    


