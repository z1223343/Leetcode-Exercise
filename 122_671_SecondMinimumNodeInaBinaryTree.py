"""
1. Brute Force (DFS)
2. Ad-Hoc

     time   space
1.   O(N)    O(H)
2.   O(N)    O(H)
"""

# solution 1:
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        unique = set()

        def dfs(root):
            if root is None:
                return
            unique.add(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        min = root.val
        min_second = float('inf')
        for x in unique:
            if min < x < min_second:
                min_second = x
        return min_second if min_second < float('inf') else -1

# solution 2:
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = float('inf')
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1