"""
1 level solution
1. DP

    time   space
1.  O()    O()
"""

# solution 1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i - coin]
        return dp[amount]

# 注意这个题 不考虑coin排列的顺序，而这个算法也是不考虑coin排列的顺序