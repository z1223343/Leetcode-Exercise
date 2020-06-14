"""

"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        r0 = len(grid)
        c0 = len(grid[0])


        def area(r, c):
            if (0 <= r < r0) and (0 <= c < c0) and ((r, c) not in seen) and grid[r][c]:
                seen.add((r, c))
                return (1 + area(r - 1, c) + area(r + 1, c) + area(r, c - 1) + area(r, c + 1))
            else:
                return 0


        areas = []
        for i in range(r0):
            for j in range(c0):
                areas.append(area(i, j))
        return max(areas)

"""

"""