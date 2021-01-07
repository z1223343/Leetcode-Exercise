"""
1. collections.Counter()

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        self.count = collections.Counter()
        self.inorder(root)
        freq = max(self.count.values())
        res = []
        for item, c in self.count.items():
            if c == freq:
                res.append(item)
        return res

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.count[root.val] += 1
        self.inorder(root.right)



# 自己写的不对。
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