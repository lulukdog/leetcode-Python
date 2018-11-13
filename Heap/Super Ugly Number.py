#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.nthSuperUglyNumber(12,[2,7,13,19]))




