#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        def bfsTree(node,level):
            if not node:
                return 

            try:
                res[level]
            except Exception:
                res.append([])

            res[level].append(node.val)

            bfsTree(node.left, level+1)
            bfsTree(node.right, level+1)

        bfsTree(root,0)

        return res


if  __name__ == '__main__':
    l = []
    try:
        l[0]
    except Exception:
        l.append([0])

    print l
    


