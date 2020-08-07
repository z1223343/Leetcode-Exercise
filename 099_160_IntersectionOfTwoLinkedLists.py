"""
1 level solution:
1. 2 pointers

time: O(m+n)   space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB
        while l1!=l2:
            l1 = l1.next if l1!=None else headB
            l2 = l2.next if l2!=None else headA
        return l1