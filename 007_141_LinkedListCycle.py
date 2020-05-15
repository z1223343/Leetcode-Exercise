"""
3 level solustions:
1. brute force (traverse): too stupid will not explain
2. hash table: traverse once, if element is seen, return True, if it is not seen, go next until to the end and return False.
    hash table 可以理解为快速读取的缓存，用空间来省时间
3. Two pointers: one slow, one fast. If there is a loop in the list. They will finally meet each other.

    Time   Space
2. O(n)     O(n)
3. O(n)     O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow = head
        fast = head.next
        while (slow!=None) and (fast!=None) and (fast.next!=None): # 注意第三个条件，很容易遗漏并导致error
            if slow!=fast:
                slow = slow.next
                fast = fast.next.next
            else:
                return True
        return False

"""
链表： linked list. "地下党“ 上级只知道自己下级的储存地址，各元素分散式存储，不需要像数组一样整块存储

我不是很明白，万一有两个数值一样的单元呢，这个算法只检测数值是否相同
"""