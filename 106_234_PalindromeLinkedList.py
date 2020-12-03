"""


"""

"""
1.Find the end of the first half.
2.Reverse the second half.
3.Determine whether or not there is a palindrome.
4.Restore the list.
5.Return the result.
"""

# solution 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 虽然题目没有要求，这里我们还是保证input最后为原状
        if not head:
            return True
        first_half_end = self.first_half_end(head)
        second_half_start = self.reverse_list(first_half_end.next)

        result = True
        first_posi = head
        second_posi = second_half_start
        while second_posi and result:
            if first_posi.val != second_posi.val:
                result = False
                break
            first_posi = first_posi.next
            second_posi = second_posi.next

        second_half_start = self.reverse_list(second_half_start)
        return result

    def first_half_end(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next: # while 写成 if 了，debug了一晚上
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


# solution 1 (2刷自己写的，没有保证input原链表保持不变）： 这里如果input is [1,2,3,4,5,6,7,8,9]，那么运行完head会变成[1,2,3,4,5,6].原因在rever_nodes这个函数，因为第一个head.next = L.next，让6之后的node都删除了，后面的循环并不影响我们的原始input，具体为什么自己想把，我想了15分钟想明白了。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if not head:
            return True

        first_half_nodes = self.get_first_half_nodes(head)
        reversed_second_half_nodes = self.reverse_nodes(first_half_nodes.next)

        first_posi = head # cannot use first_half_nodes
        second_posi = reversed_second_half_nodes
        while second_posi:  # note it should be second_posi instead of first_posi, because length(first_half)>=second_half, also first is actually head here.
            if first_posi.val != second_posi.val:
                return False
            else:
                first_posi = first_posi.next
                second_posi = second_posi.next
        return True

    def get_first_half_nodes(self, head):
        first = head
        second = head
        while first.next and first.next.next:
            first = first.next.next
            second = second.next
        return second

    def reverse_nodes(self, head):
        L = ListNode(-1)
        while head:
            L.next, head.nex