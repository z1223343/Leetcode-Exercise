"""
1. not good enough has error

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.count = 0
        self.maxcount = 0
        self.prenode = None

        def inorder(node):

            if node is None:
                return None
            inorder(node.left)
            if self.prenode is not None:
                if node.val == self.prenode:
                    self.count += 1
                    if self.count > self.maxcount:
                        self.ans = node.val
                        self.maxcount = self.count
                else:
                    self.count = 0
            else:
                self.ans = node.val
            self.prenode = node.val
            inorder(node.right)

        inorder(root)
        return [self.ans]