"""
1. Recursive (又有点bottom-up solution的意思，有点巧妙)

     time   space
1.   O(N)    O(H)
"""

# solution 1:
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        def arrow_length(root):
            if root is None:
                return 0
            left_length = arrow_length(root.left)
            right_length = arrow_length(root.right)
            left_arrow = right_arrow = 0
            if root.left and root.val == root.left.val:
                left_arrow = left_length + 1
            if root.right and root.val == root.right.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow+right_arrow)
            return max(left_arrow,right_arrow)
        arrow_length(root)
        return self.ans