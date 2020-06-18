"""
3 level solution:
1. DFS
2. BFS (其实就是用queue,和用stack很像)
3. Union Find (aka Disjoint Set) 一个崭新的算法，见后面我的分析

    time    space
1. O(M*N)  O(M*N)
2. O(M*N)  O(min(M,N))
3. O(M*N)  O(M*N)
(Note that Union operation takes essentially constant time when UnionFind is implemented with both path compression
and union by rank.)
"""

# DFS solution 1
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

# improved solution 1 (根据LeetCode solution的思路，真的time和space都快到了100%，很棒）
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(r, c):
            grid[r][c] = 0
            if (r + 1 < len(grid)) and grid[r + 1][c] == '1':
                dfs(r + 1, c)
            if (r - 1 >= 0) and grid[r - 1][c] == '1':
                dfs(r - 1, c)
            if (c + 1 < len(grid[0])) and grid[r][c + 1] == '1':
                dfs(r, c + 1)
            if (c - 1 >= 0) and grid[r][c - 1] == '1':
                dfs(r, c - 1)

        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    cnt += 1
                    dfs(r, c)
        return cnt


# solution 3.
"""
Union Find (并查集) 是一个新算法，这里了解一下
资料参考：https://blog.csdn.net/johnny901114/article/details/80721436
"""
# Java 代码实现实例（leetCode答案，但我删了两行没用的）
# class Solution {
#   class UnionFind {
#     int count; // # of connected components
#     int[] parent;
#     int[] rank;
#
#     public UnionFind(char[][] grid) { // for problem 200
#       count = 0;
#       int m = grid.length;
#       int n = grid[0].length;
#       parent = new int[m * n];
#       rank = new int[m * n];
#       for (int i = 0; i < m; ++i) {
#         for (int j = 0; j < n; ++j) {
#           if (grid[i][j] == '1') {
#             parent[i * n + j] = i * n + j;
#             ++count;
#           }
#           rank[i * n + j] = 0;
#         }
#       }
#     }
#
#     public int find(int i) { // path compression 博大精深，既查找了也压缩了，而且用了递归的形式，你品品，等于用了一个while.
#       if (parent[i] != i) parent[i] = find(parent[i]);
#       return parent[i];
#     }
#
#     public void union(int x, int y) { // union with rank
#       int rootx = find(x);
#       int rooty = find(y);
#       if (rootx != rooty) {
#         if (rank[rootx] > rank[rooty]) {
#           parent[rooty] = rootx;
#         } else if (rank[rootx] < rank[rooty]) {
#           parent[rootx] = rooty;
#         } else {
#           parent[rooty] = rootx; rank[rootx] += 1;
#         }
#         --count;
#       }
#     }
#
#     public int getCount() {
#       return count;
#     }
#   }
#
#   public int numIslands(char[][] grid) {
#     if (grid == null || grid.length == 0) {
#       return 0;
#     }
#
#     int nr = grid.length;
#     int nc = grid[0].length;
#     UnionFind uf = new UnionFind(grid);
#     for (int r = 0; r < nr; ++r) {
#       for (int c = 0; c < nc; ++c) {
#         if (grid[r][c] == '1') {
#           if (r - 1 >= 0 && grid[r-1][c] == '1') {
#             uf.union(r * nc + c, (r-1) * nc + c);
#           }
#           if (r + 1 < nr && grid[r+1][c] == '1') {
#             uf.union(r * nc + c, (r+1) * nc + c);
#           }
#           if (c - 1 >= 0 && grid[r][c-1] == '1') {
#             uf.union(r * nc + c, r * nc + c - 1);
#           }
#           if (c + 1 < nc && grid[r][c+1] == '1') {
#             uf.union(r * nc + c, r * nc + c + 1);
#           }
#         }
#       }
#     }
#
#     return uf.getCount();
#   }
# }

"""
以上是一个很标准的Union Find算法。

但我觉得他还是整麻烦了，这个答案和大部分代码都无关啊，只要一开始统计等于1的count，主function四个方向expand if等于1 count--，就完事了
我们根本不care ’parent‘内部具体的值
"""