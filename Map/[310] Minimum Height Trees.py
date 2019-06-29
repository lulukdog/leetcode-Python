#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
import collections


class Solution:
#     exceed time dfs
#     def findMinHeightTrees(self, n, edges):
#         if n == 1:
#             return [0]
#         elif n == 2:
#             return [0, 1]

#         mhts = [0] * n
#         res = []

#         tree = collections.defaultdict(list)
#         for edge in edges:
#             tree[edge[0]].append(edge[1])
#             tree[edge[1]].append(edge[0])

#         def calMaxHeight(root, fromRoot):
#             if len(tree[root]) == 1:
#                 return 0

#             maxHeight = 1
#             for v in tree[root]:
#                 if v == fromRoot:
#                     continue
#                 height = calMaxHeight(v, root) + 1
#                 if height > maxHeight:
#                     maxHeight = height

#             return maxHeight

#         for i in range(n):
#             mhts[i] = calMaxHeight(i, i)

#         minimum = max(mhts)
#         for v in mhts:
#             if v < minimum and v > 0:
#                 minimum = v

#         for i in range(n):
#             if mhts[i] > 0 and mhts[i] == minimum:
#                 res.append(i)

        # delete only on link 
        if n == 1:
            return [0]
        g = collections.defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        leaves = [i for i in g.keys() if len(g[i]) == 1]
        print(leaves)

        while n > 2:
            n -= len(leaves)
            newleaves = []
            for u in leaves:
                v = g[u]
                del g[u]
                for each in v:
                    g[each].remove(u)
                    if len(g[each]) == 1:
                        newleaves.append(each)
            leaves = newleaves
        return leaves

        return res

