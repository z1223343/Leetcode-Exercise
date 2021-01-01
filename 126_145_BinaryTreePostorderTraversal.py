"""
1. DFS (preorder)
2. Morris Traversal

     time   space
1.   O(N)    O(H)
2.   O(N)    O(H)
"""

# solution 1:
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                res.append(node.val)
        dfs(root)
        return res