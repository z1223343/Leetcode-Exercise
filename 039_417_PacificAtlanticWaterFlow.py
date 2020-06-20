"""
1 solution

DFS sfdsd
"""


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return

        self.rows = len(matrix)
        self.cols = len(matrix[0])

        canreachP = [[0] * len(matrix[0]) for _ in range(self.rows)]
        canreachA = [[0] * len(matrix[0]) for _ in range(self.rows)]

        ans = []
        for i in range(self.rows):
            self.dfs(matrix, i, 0, canreachP)
            self.dfs(matrix, i, self.cols - 1, canreachA)
        for j in range(self.cols):
            self.dfs(matrix, 0, j, canreachP)
            self.dfs(matrix, self.rows - 1, j, canreachA)
        for i in range(self.rows):
            for j in range(self.cols):
                if canreachP[i][j] and canreachA[i][j]:
                    ans.append([i, j])
        return ans

    def dfs(self, matrix, r, c, canreach):

        if canreach[r][c]:
            return
        canreach[r][c] = 1
        if r < self.rows - 1 and matrix[r + 1][c] >= matrix[r][c]:
            self.dfs(matrix, r + 1, c, canreach)
        if r > 0 and matrix[r - 1][c] >= matrix[r][c]:
            self.dfs(matrix, r - 1, c, canreach)
        if c < self.cols - 1 and matrix[r][c + 1] >= matrix[r][c]:
            self.dfs(matrix, r, c + 1, canreach)
        if c > 0 and matrix[r][c - 1] >= matrix[r][c]:
            self.dfs(matrix, r, c - 1, canreach)


# 这样不行： ！！！ 各个row会一起变化，就算是只给一个row赋值。很奇怪。
canreachP = [[0] * len(matrix[0])] * len(matrix)
canreachA = [[0] * len(matrix[0])] * len(matrix)
