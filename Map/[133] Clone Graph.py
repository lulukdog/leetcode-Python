#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        m = {}

        def clone(head):
            if not head:
                return None
            if head in m:
                return m[head]

            n = Node(head.val, [])
            m[head] = n
            for neighbor in head.neighbors:
                n.neighbors.append(clone(neighbor))
            return n

        return clone(node)
