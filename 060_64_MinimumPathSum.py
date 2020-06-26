"""
3 level solution

"""

# standard DP, but time score is 5%.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        dp = [[[] for i in range(len(grid[0]))] for i in range(len(grid))]

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif i != len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])
                else:
                    dp[i][j] = grid[i][j]

        return dp[0][0]

# improved one. but time score still 30%
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    grid[i][j] = grid[i][j] + grid[i][j + 1]
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    grid[i][j] = grid[i][j] + grid[i + 1][j]
                elif i != len(grid) - 1 and j != len(grid[0]) - 1:
                    grid[i][j] = grid[i][j] + min(grid[i][j + 1], grid[i + 1][j])

        return grid[0][0]

# 看高time score别人的solution，牛逼啊
# 少了之前繁琐的if判断
# 正向循环也行啊
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]