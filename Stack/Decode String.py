#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for k in s:
            if k !=']':
                stack.append(k)
            else:
                tempString = ''
                tempPre = stack.pop()
                while tempPre!='[':
                    tempString += tempPre[::-1]
                    tempPre = stack.pop()
                numStr = ''
                while len(stack)>0 and stack[-1] in '1234567890':
                    numStr += stack.pop()
                stack.append(tempString[::-1]*int(numStr[::-1]))
        return ''.join(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))




