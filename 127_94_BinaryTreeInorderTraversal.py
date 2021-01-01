"""
1. DFS (preorder)
2. Morris Traversal

     time   space
1.   O(N)    O(H)
2.   O(N)    O(H)
"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
        dfs(root)
        return res