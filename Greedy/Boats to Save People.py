#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        start,end = 0,len(people)-1
        needBoat = 0
        while start<=end:
        	if people[start]+people[end]>limit:
        		needBoat+=1
        		end-=1
        	else:
        		needBoat+=1
        		start+=1
        		end-=1
        return needBoat



if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats([3,5,3,4],5))






