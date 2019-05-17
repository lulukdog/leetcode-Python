# -*- coding:utf-8 -*-

from dateutil import parser
import time
import sys


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        
        d = {}

        def find(i):
            d.setdefault(i,i)
            if d[i] != i:
                d[i] = find(d[i])
            return d[i]

        def union(i,j):
            d[find(i)] = find(j)

        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    union((i-1,j,2),(i,j,0))
                if j:
                    union((i,j-1,1),(i,j,3))
                if grid[i][j] != '/':
                    union((i,j,2),(i,j,3))
                    union((i,j,0),(i,j,1))
                if grid[i][j] != '\\':
                    union((i,j,1),(i,j,2))
                    union((i,j,0),(i,j,3))

        return len(set(map(find,d)))



if __name__ == '__main__':
    s = Solution()
    print s.regionsBySlashes(["/\\","\\/"])

    




