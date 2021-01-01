"""
1. DFS (preorder)
2. Morris Traversal

     time   space
1.   O(N)    O(H)
2.   O(N)    O(H)
"""

# solution 1:
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return res