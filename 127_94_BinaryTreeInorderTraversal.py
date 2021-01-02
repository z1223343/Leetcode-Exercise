"""
1. DFS (inorder)
2. Morris Traversal (要不考虑output size，space complexity is O(1))

     time   space
1.   O(N)    O(H)
2.   O(N)    O(H)
"""

# solution 1
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

# solution 2 (可以，Morris Traversal 中序遍历和前序遍历的区别竟然就只是在curr.left is not None的情况里的if else里append换个位置.)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        curr = root
        res = []
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while (pre.right is not None) and (pre.right is not curr):
                    pre = pre.right
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res