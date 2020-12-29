"""
1. Recursive (DFS)

     time   space
1.   O(N)    O(N)
"""

# solution 1:
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
        return t1