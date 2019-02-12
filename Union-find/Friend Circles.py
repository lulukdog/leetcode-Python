#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """ 
        queue, cnt = [0], 0  # [0] 表示第一个人，题目已经给出至少一个人。 cnt 记录朋友圈的个数
        visited = [0] * len(M)  # 0 表示没有访问过，1 表示已经访问过了。
        visited[0] = 1

        while len(queue):  # 队列不为空
            i = queue.pop()  # 出队一个人
            for j in range(len(M[i])):
                if visited[j] or i == j or M[i][j] == 0:  # 访问过了，或者是自己，或者不是朋友关系，则不加
                    continue
                queue.append(j)  # 入队
                visited[j] = 1  # 此人已经访问过

            if not len(queue):  # 队列为空
                cnt += 1  # 朋友圈数 加一
                if sum(visited) < len(visited):  # 如何还有人没有被分到朋友圈
                    idx = visited.index(0)  # 继续入队一个人
                    queue.append(idx)
                    visited[idx] = 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))




