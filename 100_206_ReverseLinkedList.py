"""
1 level solution:
1. iteration

time: O(n)   space:O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            nextTmp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTmp
        return prev