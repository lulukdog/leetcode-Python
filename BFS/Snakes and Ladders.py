#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import collections

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        # n = len(board)
        # l = []
        # for i in range(n-1,-1,-1):
        #     if (n-1-i)%2==1:
        #         for j in range(len(board[i])-1,-1,-1):
        #             l.append(board[i][j])
        #     else:
        #         for j in range(0,n):
        #             l.append(board[i][j])

        # if len(l)<7:
        #     return 1

        # q = [[0,0]]
        # while q:
        #     p = q.pop(0)
        #     print p
        #     if p[1]>math.ceil((n*n)/6.0):
        #         return -1

        #     if p[0]==n*n-1:
        #         return p[1]

        #     for i in range(p[0]+1,min(p[0]+7,len(l))):
        #         if l[i] != -1 and i<len(l):
        #             q.append([l[i]-1,p[1]+1])
        #         else:
        #             q.append([i,p[1]+1])

        N = len(board)

        def get(s):  # 通过编号，获取地图的下标索引
            quot, rem = divmod(s-1, N)  # 求商：quot = a // b, 求余数： rem = a % b
            row = N - 1 - quot  # 因为是左下角开始，所以是减去
            col = rem if row%2 != N%2 else N - 1 - rem  # 确定列
            return row, col

        dist = {1: 0}  # 用于记录
        queue = collections.deque([1])
        while queue:
            s = queue.popleft()  # 出队

            if s == N*N:
                return dist[s]

            for s2 in range(s+1, min(s+6, N*N) + 1):  # 向下扩展子节点，判断入队
                r, c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in dist:
                    dist[s2] = dist[s] + 1
                    queue.append(s2)  # 入队
        return -1



if __name__ == '__main__':
    solu = Solution()
    # board = [
    #     [-1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1],
    #     [-1, 35, -1, -1, 13, -1],
    #     [-1, -1, -1, -1, -1, -1],
    #     [-1, 15, -1, -1, -1, -1]]
    board = [[-1,-1,128,-1,-1,-1,136,-1,-1,-1,109,-1],[-1,-1,-1,-1,-1,103,-1,-1,56,10,-1,-1],[-1,-1,-1,-1,-1,-1,116,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,50,-1,67,107],[-1,40,-1,-1,-1,20,-1,59,-1,67,-1,-1],[-1,-1,-1,-1,-1,-1,112,133,111,-1,-1,-1],[-1,-1,112,-1,74,-1,-1,-1,-1,-1,-1,-1],[23,-1,115,-1,129,126,-1,-1,-1,-1,-1,-1],[106,143,81,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,26,102,1,29],[26,-1,-1,-1,-1,-1,-1,-1,27,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
    print(solu.snakesAndLadders(board))



