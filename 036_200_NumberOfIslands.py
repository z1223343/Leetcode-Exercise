"""


"""

# 自己写的, 模仿上一题DFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        seen = set()
        area_list = []

        def area(r, c):
            if ((r, c) not in seen) and (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and grid[r][c] == "1": # Note,这里故意把(0 <= r < len(grid)) and (0 <= c < len(grid[0]))放在grid[r][c] == "1"，不然会出error。
                seen.add((r, c))
                return (1 + area(r - 1, c) + area(r + 1, c) + area(r, c - 1) + area(r, c + 1))
            else:
                return 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if area(r, c):
                    cnt += 1
        return cnt
# 这个题和上个不一样哈，这个input都是“1” “0” 字符串格式的。
"""

"""