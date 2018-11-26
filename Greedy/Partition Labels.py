#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        m = {}
        for i in range(len(S)):
            m[S[i]] = i

        start = 0
        res = []
        last = 0
        for i in range(len(S)):
            last = max(last,m[S[i]])
            if last==i:
                res.append(i-start+1)
                start = i+1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels('ababcbacadefegdehijhklij'))




