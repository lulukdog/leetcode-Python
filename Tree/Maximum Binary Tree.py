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
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        maxNum = max(nums)
        index = nums.index(maxNum)
        root = TreeNode(maxNum)

        # 递归添加node
        def createNode(node,lList,rList):
            if lList:
                lMax = max(lList)
                lIndex = lList.index(lMax)
                node.left = TreeNode(lMax)
                createNode(node.left,lList[0:lIndex],lList[lIndex+1:len(lList)])

            if rList:
                rMax = max(rList)
                rIndex = rList.index(rMax)
                node.right = TreeNode(rMax)
                createNode(node.right,rList[0:rIndex],rList[rIndex+1:len(rList)])

        createNode(root,nums[0:index],nums[index+1:len(nums)])

        return root


if  __name__ == '__main__':
    s = Solution()
    s.constructMaximumBinaryTree([3,2,1,6,0,5])
    


