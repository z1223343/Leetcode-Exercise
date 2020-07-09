"""
2 solution
1. DP (knapsack problem)
2. DFS
"""

# solution 1：
"""
先来一个推导，转化成01背包subset sum问题，就和上一题目非常相似了:
                  sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                       2 * sum(P) = target + sum(nums)
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum_list = sum(nums)
        if (S+sum_list)%2 != 0 or sum_list<S:
            return 0
        W = (S+sum_list)//2
        dp = [0]*(W+1)
        dp[0] = 1
        for i in nums:
            for j in range(W,i-1,-1):
                dp[j] = dp[j] + dp[j-i]
        return dp[W]

# solution 2:
# 先欠着