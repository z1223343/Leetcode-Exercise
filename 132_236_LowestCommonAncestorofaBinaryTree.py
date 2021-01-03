"""
1. Recursive （bottom-up traversal, first left or right does not matter)
2. Iterative (using parent pointers)

     time   space
1.   O(N)    O(H)
2.   O(N)    O(N)
"""

# solution 1: (这个方法不敢找没找到答案，都会完全遍历一遍，时间上有所浪费)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(root):
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)
            mid = (root == p) or (root == q)
            if mid+left+right >= 2:
                self.ans = root
            return mid or left or right
        dfs(root)
        return self.ans

# solutiion 1 另一种写法，应该是更快一点儿，来自于solution comments section，但这个也要完全遍历啊..
# 这个solution 背后的思想也挺有意思，算法是如果这个node的双手都不是0，则返回自己，如果有一个是0，则返回另一只手，这样迭代上去结果一定是对的。
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            ans = root
        else:
            ans = left if left is not None else right
        return ans

# solution 2:
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:  # p is not in parent 会报错 这不是英语。
            node = stack.pop()

            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node

        ancestors = set()
        while p:
            ancestors.add(parent[p])
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q



