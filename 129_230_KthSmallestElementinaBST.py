"""
1. Inorder Traversal

     time   space
1.   O(N)    O(H)
"""

# solution 1:
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nodelist = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            nodelist.append(root.val)
            inorder(root.right)
        inorder(root)
        return nodelist[k-1]