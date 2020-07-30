"""
1 level solution:
1. DP

    time    space
1.  O(mn)   O(mn)
"""

# solution 1:
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n * m == 0:
            return n + m

        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i - 1][j]
                up = dp[i][j - 1]
                leftup = dp[i - 1][j - 1]
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(left + 1, up + 1, leftup)
                else:
                    dp[i][j] = min(left + 1, up + 1, leftup + 1)
        return dp[-1][-1]