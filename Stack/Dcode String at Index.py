#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        ''' 时间太长，内存太大
        def checkIsOverLength(s,K):
            if len(s)>K:
                return True
            else:
                return False

        s = ''
        for v in S:
            if v.isdigit():
                s = s*int(v)
                if checkIsOverLength(s,K):
                    break
            else:
                s+=v

        return s[K-1]
        ''' 
        stack = []
        s = ''
        t = K
        for i in range(0,len(S)):
            if S[i].isdigit():
                if stack:
                    stack.append([s,(stack[-1][1]+len(s))*int(S[i])])
                else:
                    stack.append([s,len(s)*int(S[i])])
                if stack[-1][1]>=K:
                    break
                s = ''
            else:
                s += S[i]

        print(stack)
        for i in range(len(stack)-1,-1,-1):
            if i>=1 and t>=stack[i-1][1]:
                t %= stack[i-1][1] + len(stack[i][0])
                if t>len(stack[i][0]):
                    return stack[i][0][t-stack[i][1]-1]
                    continue
                else:
                    if not stack[i][0]:
                        t %= stack[i-1][1]
                    else:
                        return stack[i][0][t]
            else:
                print(stack[i][0][t-1])
                return stack[i][0][t-1]



if __name__ == '__main__':
    s = Solution()
    print(s.decodeAtIndex("leet2code3", 10))




