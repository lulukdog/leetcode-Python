#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.defaultdict(int)
        for num in nums:
            d[num]+=1

        for key in d:
            if d[key]==1:
                return key



if __name__ == '__main__':

    s = Solution()
    print(s.singleNumber([2,2,3,2]))



