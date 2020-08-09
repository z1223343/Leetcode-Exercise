"""
2 level solution:
1. recursion
2. iteration

    time  space
1.  O(N)    O(N)
2.  O(N)    O(1)
"""

# solution 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev_node = dummy

        while head != None and head.next != None:
            first_node = head
            second_node = head.next

            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = first_node.next
        return dummy.next


"""
1. why dummy: cuz head will be changed by head=first_node.next, 循环就是跟着head走的
2. why dummy.next=head, 其实这样更加方便，就是说prev_node不收corner case 影响。
"""

# 注意啊此题的题干有：You may not modify the values in the list's nodes, only nodes itself may be changed.
# 不然直接就用一下解法：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            tmp = first_node.val
            first_node.val = second_node.val
            second_node.val = tmp

            head = second_node.next

        # Return the new head node.
        return dummy.next