"""
1. DFS (preorder)
2. Morris Traversal (要不考虑output size，space complexity is O(1)

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

# solution 2: (挖槽自己写出来的，和答案简直每一行都一样，我牛逼)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        res = []
        while node:
            if node.left is None:
                res.append(node.val)
                node = node.right

            else:
                predecessor = node.left
                while (predecessor.right is not None) and (predecessor.right is not node):
                    predecessor = predecessor.right
                if predecessor.right is None:
                    res.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right
        return res


"""
DFS 总结：
DFS 分为







BFS 需要结合队列存储结构，即collections.deque  deque.append()   deque.popleft()
"""