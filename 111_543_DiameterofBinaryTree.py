"""
1. DFS (recursion)

     time   space
1.   O(N)    O(N)
"""

# solution 1:
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(root):
            if not root:
                return 0
            else:
                left = depth(root.left)
                right = depth(root.right)
                self.ans = max(left+right,self.ans)
                return max(left,right)+1
        depth(root)
        return self.ans