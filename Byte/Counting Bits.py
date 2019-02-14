#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def countOne(n):
            count = 0
            while n>0:
                count += 1 if n&1==1 else 0
                n = n>>1
            return count

        res = []
        for i in range(num+1):
            res.append(countOne(i))

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(2))



