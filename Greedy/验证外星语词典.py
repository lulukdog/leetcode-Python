#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d,i = {},0
        for w in order:
            d[w] = i
            i+=1


        def cmpFun(v1,v2):
            minLength = min(len(v1),len(v2))
            for i in range(minLength):
                if d[v1[i]] < d[v2[i]]:
                    return True
                elif d[v1[i]] == d[v2[i]]:
                    continue
                else:
                    return False

            if len(v1)>minLength:
                return False
            else:
                return True


        n = 1
        while n<len(words):
            if not cmpFun(words[n-1],words[n]):
                return False
            n+=1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))






