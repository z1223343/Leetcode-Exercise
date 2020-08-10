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
        if fast.next and fast.next.next:
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