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
            l1 = l1.next if l1!=None else headB  # 注意这里l1.next!=None就不行了，因为如果headAB不一样长，那么如何没有交叉点会无限循环下去，而如果headAB一样长的话，就循环一个长度就行了，不需要A->B B->A调换，综上l1!=None正确。
            l2 = l2.next if l2!=None else headA
        return l1