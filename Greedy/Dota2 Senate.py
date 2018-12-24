#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import collections

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        q_r, q_d = collections.deque(), collections.deque()
        n = len(senate)
        for i, s in enumerate(senate):
            if s == "R":
                q_r.append(i)
            else:
                q_d.append(i)
        while q_r and q_d:
            r = q_r.popleft()
            d = q_d.popleft()
            if r < d:
                q_r.append(r + n)
            else:
                q_d.append(d + n)
        return "Radiant" if q_r else "Dire"

if __name__ == '__main__':
    s = Solution()
    print(s.predictPartyVictory('RDDD'))






