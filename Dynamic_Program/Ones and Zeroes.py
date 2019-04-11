#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import re

class Solution():
    def findMaxForm(self,strs,m,n):
        # l = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # for str in strs:
        #     zeros = str.count("0",0,len(str))
        #     ones = str.count("1",0,len(str))
        #     for i in range(m,zeros-1,-1):
        #         for j in range(n,ones-1,-1):
        #             l[i][j] = max(l[i][j],l[i-zeros][j-ones]+1)
        #             print(i,j,zeros,ones,l[i][j])
        # return l[m][n]

        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # for str in strs:
        #     zeros, ones = 0, 0
        #     for c in str:
        #         if c == "0":
        #             zeros += 1
        #         elif c == "1":
        #             ones += 1
        #     for i in range(m, zeros - 1, -1):
        #         for j in range(n, ones - 1, -1):
        #             dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        #             print(i,j,zeros,ones,dp[i][j])
        # return dp[m][n]

        counter = [[i.count('0'), i.count('1')] for i in strs]
        s1 = sorted(counter,key=lambda x:min(x[0],x[1]))
        s2 = sorted(counter,key=lambda x:min(m-x[0],n-x[1]),reverse=True)
        print(s1,s2)
        return max(self._findMaxForm(s1, m, n),self._findMaxForm(s2, m, n))

    def _findMaxForm(self, s, m, n):
        count = 0
        for k in s:
            if m >= k[0] and n >= k[1]:
                count += 1
                m -= k[0]
                n -= k[1]
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxForm(["10","0001","111001","1","0"],5,3))
