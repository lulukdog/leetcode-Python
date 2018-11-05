#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for value in tokens:
            if value in '+-*/':
                b = int(s.pop())
                a = int(s.pop())
                if value=='+':
                    s.append(a+b)
                elif value=='-':
                    s.append(a-b)
                elif value=='*':
                    s.append(a*b)
                elif value=='/':
                    c = a/b
                    if c<0 and a%b!=0:
                        c += 1
                    s.append(c)
            else:
                s.append(value)
        return int(s[0])




if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["4","-2","/","2","-3","-","-"]))




