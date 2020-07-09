"""
1 level solution:
1. DP (knapsack problem)
"""

# solution 1. (想想感觉是逻辑是对的，再想想又不知道它为什么是对的，但自己想的话可能想不出来这么解，牛逼。
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_list = sum(nums)
        if sum_list%2 != 0:
            return False
        W = sum_list//2
        dp = [False]*(W+1)
        dp[0] = True
        for i in nums:
            for j in range(W,i-1,-1): # 就这一行，全是细节
                dp[j] = dp[j] or dp[j-i]
        return dp[W]
# 有更快的解法，好像是DFS，先欠着