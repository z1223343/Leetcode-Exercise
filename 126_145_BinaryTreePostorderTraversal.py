"""
1. DFS (postorder)
2. Iterative Preorder Traversal: Tweak the Order of the Output
Morris Traversal 好像不太行

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