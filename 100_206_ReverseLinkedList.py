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

# solution 2：
# csdn 看到的野路子牛逼解法，对连续赋值有更深的理解
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        L= ListNode(float('-inf'))
        while head:
            L.next,head.next,head = head,L.next,head.next
        return L.next