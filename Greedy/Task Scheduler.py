#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        l = [0]*26
        for v in tasks:
        	l[ord(v)-65]+=1

        l.sort(reverse = True)
        sameCount = 0
        for v in l:
        	if v==l[0]:
        		sameCount += 1
        	else:
        		break

        return max(len(tasks),(l[0]-1)*(n+1)+sameCount)


        



if __name__ == '__main__':
    s = Solution()
    print(s.leastInterval(["A","A","A","B","B","B"], 2))






