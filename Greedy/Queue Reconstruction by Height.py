#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def sortPeople(p1,p2):
            if p1[0] == p2[0]:
                return cmp(p1[1],p2[1])
            else:
                return cmp(p2[0],p1[0])

        people.sort(sortPeople)
        res = []
        for v in people:
            res.insert(v[1],v)
        return res




if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))





