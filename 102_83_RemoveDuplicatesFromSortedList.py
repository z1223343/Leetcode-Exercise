"""
1 level solution:
1. Straight-Forward Approach

time O(n)   space O(1)
"""

# solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr != None and curr.next != None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next # 一个有意思的点就是，这里curr=curr.next.next不行，甚至这个代码改变不了head。只有curr.next才可以改变head。
            else:
                curr = curr.next
        return head