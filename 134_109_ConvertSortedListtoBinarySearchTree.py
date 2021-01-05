"""
1. Recursion
2. Recursion + Conversion to Array
3.

     time   space
1.   O(N)    O(H)
2.   O(N)    O(N)
3.   O(N)    O()
"""

# solution 1:
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        mid = self.findMiddle(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

    def findMiddle(self, head):
        prePtr = None
        slowPtr = head
        fastPtr = head

        while fastPtr.next.next is not None:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        if prePtr:
            prePtr.next = None
        return slowPtr

# solution 2:
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def mapListToValues(head):
            vals = []
            while head:
                vals.append(head.val)
                head = head.next
            return vals

        def convertListtoBST(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(values[mid])
            node.left = convertListtoBST(left, mid - 1)
            node.right = convertListtoBST(mid + 1, right)
            return node

        values = mapListToValues(head)
        root = convertListtoBST(0, len(values) - 1)
        return root

# solution 3:

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findSize(self.

            head)
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
            return c

    def sortedListToBST(slef, head):
        size = self.findSize(head)

        def convert(1, r):
            nonlocal head

            if l > r:
                return None




"""
==用于判断数值是否相等，因此对于六大基本数据类型而言，相同的值即可判定相等。而对于其他类的实例化对象而言，
存储和比较的可以认为是内存地址或者id，因此此时即使拥有相同属性也会因为id不同而被判定为不相等。
is，这是用于直接比较二者的地址是否相同
"""