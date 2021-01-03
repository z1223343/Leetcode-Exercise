"""
1. Inorder Traversal
2. Morris Traversal (左右遍历颠倒)

     time   space
1.   O(N)    O(H)
2.   O(N)    O(1)
"""

# solution 1:
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        curr_sum = 0

        def reverseinorder(node):
            nonlocal curr_sum  # 我就奇了怪了，上一题一样的中间变量 数组怎么就不用声明nonlocal
            if node is None:
                return None

            reverseinorder(node.right)
            curr_sum += node.val  # 注意啊这句也应该在inorder(node.right)后面
            # node.val += curr_sum   # 注意啊这样子不行
            node.val = curr_sum
            reverseinorder(node.left)

        reverseinorder(root)
        return root


# solution 2:
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        curr_sum = 0
        node = root
        while node:
            if node.right is None:
                curr_sum += node.val
                node.val = curr_sum
                node = node.left

            else:
                pre = node.right
                while (pre.left is not None) and (pre.left is not node):
                    pre = pre.left
                if pre.left is None:  # wocao，我一开始写的 if pre is None: 结果一直是原二叉树，debug了半天
                    pre.left = node
                    node = node.right
                else:
                    pre.left = None
                    curr_sum += node.val
                    node.val = curr_sum
                    node = node.left
        return root