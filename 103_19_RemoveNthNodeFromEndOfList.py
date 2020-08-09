"""
2 level solution:
1. two-pass solution
2. one-pass solution

    time  space
1.  O(L)   O(1)
2.  O(L)   O(1)
"""

# solution 2:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        first = dummy
        second = dummy
        dummy.next = head
        for i in range(1,n+2):
            first = first.next
        while first!=None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next