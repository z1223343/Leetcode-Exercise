"""
1. inorder traversal

     time     space
1.   O(N)      O(N)
"""

# solution 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prenode = None
        self.minidiff = float('inf')

        def inorder(node):

            if node is None:
                return None
            inorder(node.left)

            if self.prenode is not None:
                diff = node.val - self.prenode
                self.minidiff = min(self.minidiff, diff)

            self.prenode = node.val
            inorder(node.right)

        inorder(root)
        return self.minidiff