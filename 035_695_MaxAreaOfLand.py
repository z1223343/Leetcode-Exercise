"""
2 level solution:
1. DFS (Depth First Search) (Recursive)
2. DFS (Iterative) (用stack)

   time space
1. O(R*C)  O(R*C)
2. O(R*C)  O(R*C)
"""
# solution 1
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

# solution 2
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        seen = set()

        for r0 in range(len(grid)):
            for c0 in range(len(grid[0])):
                if grid[r0][c0] == 1 and ((r0, c0) not in seen):
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    shape = 0
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for r1, c1 in ((r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)):
                            if (0 <= r1 < len(grid)) and (0 <= c1 < len(grid[0])) and grid[r1][c1] == 1 and (
                                    (r1, c1) not in seen):
                                stack.append((r1, c1))
                                seen.add((r1, c1))
                    ans = max(ans, shape)
        return ans

"""
solution 2 难道不是 BFS??? 按照我的理解solution 2是BFS.
"""