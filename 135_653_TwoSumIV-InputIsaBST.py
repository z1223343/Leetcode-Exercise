"""
1. convert to array then use two pointers to find sum (sub problem No.167) (This solution is Leetcode solution 3: Using BST.

     time     space
1.   O(N)      O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        def inorder(root):
            nonlocal nums
            if root is None:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        inorder(root)
        l = 0
        r = len(nums)-1
        while l<r:
            tmp = nums[l]+nums[r]
            if tmp == k:
                return True
            else:
                if tmp>k:
                    r -= 1
                else:
                    l += 1
        return False