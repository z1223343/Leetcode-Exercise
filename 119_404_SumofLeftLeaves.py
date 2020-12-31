"""
1. Recursive (DFS)
2. Morris Tree Traversal (pre-order)

     time   space
1.   O(N)    O(N)
2.   O(N)    O(1)
"""

# solution 1:
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def helper(root, is_left):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return root.val if is_left else 0
            return helper(root.left, True) + helper(root.right, False)

        return helper(root, False)


# solution 2 (我承认，我看了半天没看懂)
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        total_sum = 0
        current_node = root
        while current_node is not None:
            if current_node.left is None:
                current_node = current_node.right
            else:
                previous = current_node.left
                if previous.left is None and previous.right is None:
                    total_sum += previous_node.val
                while previous.right is not None and previous.right is not current_node:
                    previous = previous.right
                if previous.right is None:
                    previous.right = current_node
                    current_node = current_node.left
                else:
                    pervious.right = None
                    current_node = current_node.right
        return total_sum