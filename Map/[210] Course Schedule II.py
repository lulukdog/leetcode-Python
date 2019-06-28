class Solution:
    def findOrder(self, n, prerequisites):
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        visiteL = [0] * n
        res = []

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
            res.append(i)
            return True

        for i in range(n):
            if not dfs(i):
                return []

        return res
