#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         res += bin(nums[i]^nums[j]).count('1')

        # return res

        res = 0
        for pos in range(32):
            bitCount = 0
            for i in range(len(nums)):
                bitCount += (nums[i] >> pos) & 1
            res += bitCount * (len(nums) - bitCount)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.totalHammingDistance([4, 14, 2]))




