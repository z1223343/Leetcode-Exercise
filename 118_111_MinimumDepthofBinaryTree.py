


# solution 1 我自己写的solution,很显然不够快
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = float('inf')
        def helper(root ,depth):
            nonlocal ans
            if root is None:
                return
            if root.left is None and root.right is None:
                ans = min(ans ,dept h +1)
                return
            depth += 1
            helper(root.left ,depth)
            helper(root.right ,depth)

        helper(root ,0)
        return ans

# solution 2 (来自one comment in leetcode solution 做法非常简洁）
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right)+1
        if root.right is None:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1

# 但我觉得理论上最快的方法是不是用BFS啊