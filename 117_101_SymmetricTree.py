"""
1. Recursive (DFS)

     time   space
1.   O(N)    O(N)
"""

# solution 1: (用一个helper函数，root输入两次用于比较)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def isMirror(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root, root)