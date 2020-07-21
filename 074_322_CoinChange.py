"""
1 level solution:
1. DP (complete backpack problem)

    time    space
1.  O(S*n)  O(S)
"""

# solution 1 (from Github guidline)
# 完全背包问题
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [0] * (amount + 1)
        for coin in coins:
            for i in range(coin, amount + 1):
                if i == coin:
                    dp[i] = 1
                elif dp[i] == 0 and dp[i - coin] != 0:
                    dp[i] = dp[i - coin] + 1
                elif dp[i] != 0 and dp[i - coin] != 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == 0 else dp[amount]

# solution 1: （from LeetCode solution，这样写也很漂亮啊)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# 我打赌这个题DFS做也行，不光这个题，01背包的所有题应该都可以用DFS来解，但对于完全背包，数组一开始要sort一下。