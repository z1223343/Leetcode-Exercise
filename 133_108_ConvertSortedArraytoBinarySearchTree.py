"""
1. Recursive (preorder)

     time   space
1.   O(N)    O(H)
"""

# solution 1:
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left,right):
            if left>right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left,mid-1)
            root.right = helper(mid+1,right)
            return root
        root = helper(0,len(nums)-1)
        return root