# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ln = ListNode(0)
        res = ln
        up = 0
        while l1 or l2:
            v1,v2 = 0,0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            unit = 0
            nowSum = v1+v2+up
            if (nowSum)>9:
                up = 1
                unit = nowSum-10
            else:
                up=0
                unit = nowSum
            
            ln.next = ListNode(unit)
            ln = ln.next
        
        if up==1:
            ln.next = ListNode(1)
        
        return res.next
            
                
