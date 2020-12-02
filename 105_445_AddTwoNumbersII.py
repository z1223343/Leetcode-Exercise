"""
1 level solution:
1. convert to number and then create new listnode
"""

# solution 1: # 没有按照Leetcode solution，但我感觉这个解法更棒
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = 0
        n2 = 0
        while l1:
            n1 = n1 * 10 + l1.val
            l1 = l1.next
        while l2:
            n2 = n2 * 10 + l2.val
            l2 = l2.next
        n3 = n1 + n2

        if n3 == 0:
            return ListNode(0, None)
        result = None
        while n3: # or n3>0
            result = ListNode(n3 % 10, result)
            n3 //= 10
        return result