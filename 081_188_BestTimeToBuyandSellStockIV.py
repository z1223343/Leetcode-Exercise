"""
1 level solution:
1. DP

    time                       space
1.  O(nk) or O(n) if 2k>n      O(nk)
"""

# solution 1
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k < 1:
            return 0

        res = 0
        if k * 2 >= len(prices):
            for i, j in zip(prices[:-1], prices[1:]):
                res += max(0, j - i)
            return res

        dp = [[[float('-inf')] * 2 for i in range(0, k + 1)] for j in range(0, len(prices))]

        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k + 1):
                # transition equation
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                # you can't hold stock without any transaction
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

    res = max(dp[-1][j][0] for j in range(k + 1))
    return res

"""
此题建议重做：
我很震惊： 1. why res = max(..
2. 为什么要赋初始值
3. 为什么要分j>o 情况
"""