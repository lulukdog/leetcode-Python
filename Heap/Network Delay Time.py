#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import heapq

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        ''' Floyd
        INF = 0x3f3f3f3f
        dist = [[INF] * N for _ in range(N)]

        for time in times:
            u = time[0]
            v = time[1]
            w = time[2]
            dist[u-1][v-1] = w

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
                    # print(i+1,j+1,dist[i][j])

        res = 0
        for i in range(N):
            if i != K-1:
                res = max(res, dist[K-1][i])

        return -1 if res>=INF else res
        ''' 
        pq = []
        INF = float('inf')
        dist = [INF] * N

        graph = [[] for _ in range(N)]

        for time in times:
            graph[time[0] - 1].append((time[1] - 1, time[2]))

        heapq.heappush(pq, (0, K - 1))
        dist[K - 1] = 0

        while len(pq):
            cur = heapq.heappop(pq)
            for to, cost in graph[cur[1]]:
                if (dist[to] > dist[cur[1]] + cost):
                    dist[to] = cost + dist[cur[1]]
                    heapq.heappush(pq, (dist[to], to))

        ans = 0
        for i in range(N):
            if i == K - 1:
                continue
            else:
                ans = max(ans, dist[i])

        return -1 if ans >= INF else ans


if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTime([[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]],5,3))




