#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1,a2 = a.split('+')
        b1,b2 = b.split('+')
        a2 = a2[:-1]
        b2 = b2[:-1]
        a1 = int(a1)
        a2 = int(a2)
        b1 = int(b1)
        b2 = int(b2)
        res1 = a1*b1-a2*b2
        res2 = a1*b2+a2*b1
        return str(res1)+'+'+str(res2)+'i'


if  __name__ == '__main__':
    s = Solution()
    print(s.complexNumberMultiply("1+-1i", "1+-1i"))
    


