#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        t = head
        while t:
            l.append(t.val)
            t = t.next
        l.sort()
        t = head
        i = 0
        for i in range(len(l)):
            t.val = l[i]
            t = t.next
        return head



if __name__ == '__main__':
    s = Solution()
    a1 = ListNode(4)
    a2 = ListNode(2)
    a3 = ListNode(1)
    a4 = ListNode(3)
    a1.next = a2
    a2.next = a3
    a3.next = a4


    s.sortList(a1)
    a = a1
    while a:
        print(a.val)
        a = a.next




