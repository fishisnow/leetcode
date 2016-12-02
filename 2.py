#coding:utf-8
"""
#给你两个链表表示两个非负数字。数字存储在相反的顺序和每个节点包含一个数字。添加两个数字并返回一个链表。
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8

# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
"""
设x为l1节点值, y为l2节点值, 若为空则为0
sum = x + y + carry
carry = sum / 10 
sum = sum % 10

循环结束后，判断carry是否为1, 是则添加数字1
"""
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        cat = 0
        head = l
        while(l1 is not None or l2 is not None):
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            sum = val1 + val2 + cat
            if(sum > 9):
                sum = sum % 10
                l.next = ListNode(sum)
                l = l.next
                cat = 1
            else:
                l.next = ListNode(sum)
                l = l.next
                cat = 0
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
            
        if cat == 1:
            l.next = ListNode(1)

        return head.next

