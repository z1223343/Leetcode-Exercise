"""
4 level solutions
1. brute force
2. DP
3. Greedy
4. BFS
5. Mathematics

2. time O(n*n**(1/2))   space O(n)
"""

# soulution 4: refer to No.033
# 我都做过了一遍了还是看了一会儿才看懂BFS思路

# soulution 2: 这里只看DP
# 我感觉我的思维还是对DP很迟钝，需要对DP的思想有更深的了解
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_numbers = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 很重要

        for i in range(1, n + 1):
            for square in square_numbers:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]
