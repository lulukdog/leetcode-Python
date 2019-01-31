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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        new_s = ListNode(None)
        new_s.next = ListNode(head.val)
        cur = head.next
        while cur:
            insert_node = ListNode(cur.val)
            new_cur = new_s.next
            pre = new_s
            while new_cur:
                if new_cur.val >= insert_node.val:
                    insert_node.next = new_cur
                    pre.next = insert_node
                    break
                elif new_cur.next is None:
                    new_cur.next = insert_node
                    break
                pre = new_cur
                new_cur = new_cur.next
            cur = cur.next
        return new_s.next



if __name__ == '__main__':
    s = Solution()
    a1 = ListNode(4)
    a2 = ListNode(2)
    a3 = ListNode(1)
    a4 = ListNode(3)
    a1.next = a2
    a2.next = a3
    a3.next = a4

    a = s.insertionSortList(a1)
    while a:
        print(a.val)
        a = a.next




