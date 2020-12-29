"""
1. Recursive (DFS)

     time   space
1.   O(N)    O(N)
"""

# solution 1: (真的骚,竟然没有用额外的函数帮助，甚至没有用额外的变量记录sum)
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if root is None:
            return False

        sum = sum - root.val
        if root.left is None and root.right is None:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)