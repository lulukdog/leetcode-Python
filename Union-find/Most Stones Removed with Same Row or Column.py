#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n=len(stones)
        fa=list(range(n+1))
        
        def find(i):
            while fa[i]!=i:
                fa[i]=fa[fa[i]]
                i=fa[i]
            return i
        
        def union(i,j):
            fi=find(i)
            fj=find(j)
            fa[fi]=fj
        
        s=set([tuple(t) for t in stones])
        for i in range(n):
            for j in range(i+1,n):
                xi,yi=stones[i]
                xj,yj=stones[j]
                if xi==xj or yi==yj: 
                    union(i,j)
        
        d={}
        for i in range(n):
            fi=find(i)
            d[fi]=d.get(fi,0)+1
        res=0
        print(d)
        for i in d:
            res+=d[i]-1
        return res


if __name__ == '__main__':
    s=Solution()
    print(s.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))




