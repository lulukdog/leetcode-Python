#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,index = 0,0
        while (i!=-1 and index<len(s)):
            i = t.find(s[index],i)
            if i!=-1:
                index+=1
                i+=1
        return index==len(s)


if __name__ == '__main__':
    s = Solution()
    k = "abc"
    t = "ahbgdc"
    print(s.isSubsequence(k,t))






