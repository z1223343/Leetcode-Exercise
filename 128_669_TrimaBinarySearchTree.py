"""
1. Recursive

     time   space
1.   O(N)    O(H)
"""

# solution 1:
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        def trim(root):
            if root is None:
                return None
            if root.val < low:
                return trim(root.right)
            elif root.val > high:
                return trim(root.left)
            else:
                root.left = trim(root.left)
                root.right = trim(root.right)
                return root

        return trim(root)

# solution 1 或者这么写，不用子函数，但要多传几遍low,high变量。
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right,low,high)
        elif root.val > high:
            return self.trimBST(root.left,low,high)
        else:
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
            return root