"""
1 solution:
1. Dynamic programming

time: O(n)   space: O(1)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        pre1 = 0
        pre2 = 0
        curr = 0
        for i in range(len(nums)):
            curr = max(pre2+nums[i],pre1)  # 思想牛的
            pre2 = pre1
            pre1 = curr
        return curr