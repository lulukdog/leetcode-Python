#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
import collections


class Solution:
    def canFinish(self, n, prerequisites):
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        visiteL = [0] * n

        def dfs(i):
            if visiteL[i] == 1:
                return False
            if visiteL[i] == 2:
                return True

            visiteL[i] = 1
            for v in graph[i]:
                if not dfs(v):
                    return False

            visiteL[i] = 2
            return True

        for i in range(n):
            if not dfs(i):
                return False

        return True

