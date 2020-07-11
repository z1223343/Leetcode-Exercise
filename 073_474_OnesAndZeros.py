"""
1 level solution:
1. DP (knapsack problem)

time:  O(l*m*n)    space:  O(m*n)
"""

# solution 1:
# 多维费用01背包问题
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count01(string):
            count_1 = 0
            count_0 = 0
            for i in range(0, len(string)):
                if string[i] == '0':
                    count_0 += 1
                else:
                    count_1 += 1
            return count_0, count_1

        dp = [[0] * (m + 1) for i in range(0, n + 1)]
        for string in strs:
            count0, count1 = count01(string)
            for i in range(m, count0 - 1, -1):
                for j in range(n, count1 - 1, -1):
                    dp[j][i] = max(dp[j][i], 1 + dp[j - count1][i - count0])
        return dp[n][m]

# 此题建议再多练练