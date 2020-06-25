"""
1 solution:
1. Dynamic programming
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        return max(self.dp(nums, 0, n - 2), self.dp(nums, 1, n - 1))

    def dp(self, nums, start, end):
        pre1 = 0
        pre2 = 0
        for i in range(start, end + 1):
            curr = max(pre2 + nums[i], pre1)
            pre2 = pre1
            pre1 = curr
        return curr