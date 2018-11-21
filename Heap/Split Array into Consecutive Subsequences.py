#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import heapq

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = {}
        need = {}
        for i in range(nums[0],nums[-1]+3):
            need[i] = 0

        for num in nums:
            if l.has_key(num):
                l[num]+=1
            else:
                l[num] = 1

        l[nums[-1]+1] = 0
        l[nums[-1]+2] = 0

        for num in nums:
            if l[num]==0:
                continue
            elif need[num]>0:
                l[num] -= 1
                need[num] -= 1
                need[num+1] += 1
            elif l.has_key(num+1) and l.has_key(num+2) and l[num+1]>0 and l[num+2]>0:
                l[num]-=1
                l[num+1]-=1
                l[num+2]-=1
                need[num+3]+=1
            else:
                return False
        return True



if __name__ == '__main__':

    s = Solution()
    print(s.isPossible([1,2,3,3,4,4,5,5]))




