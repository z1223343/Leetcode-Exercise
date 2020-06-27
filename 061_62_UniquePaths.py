"""
3 level solutions:
1. recursive solution
2. Dynamic Programming
3. Math (python3 only)

    time    space
1.  very large
2.  O(MN)   O(MN)
3.  O((M+N)(log(M+N)loglog(M+N))**2)  O(1)
"""

# solution 1：
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
"""
This solution is very inefficient: for example
input:
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
The processing times in each cell:
70 35 15 5 1
35 20 10 4 1
15 10 6  3 1
5  4  3  2 1
1  1  1  1 0
So, it's like exponential increasing
"""

# solution 2:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

# solution 3:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2)//factorial(n-1)//factorial(m-1)

"""
此题转换为一个组合问题。
C^h_(h+v) = (h+v)!/(h!v!) 卧槽我怎么不知道这数学公式
"""



