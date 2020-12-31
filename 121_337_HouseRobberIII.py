"""
1. Recursive (又有点bottom-up solution的意思)

     time   space
1.   O(N)    O(H)
"""

# solution 1:
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(root):
            if root is None:
                return [0,0]
            left = helper(root.left)
            right = helper(root.right)
            rob_curr = root.val+left[1]+right[1]
            unrob_curr = max(left)+max(right)
            return [rob_curr,unrob_curr]
        return max(helper(root))