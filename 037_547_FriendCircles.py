"""
3 level solution:
1. DFS
2. BFS (用stack(queue))
3. Union Find

"""

# DFS solution 1:
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = []
        count = 0

        def dfs(r):
            for c in range(len(M[0])):
                if c not in visited and M[r][c]:
                    visited.append(c)
                    dfs(c)

        for r in range(len(M)):
            if r not in visited:
                count += 1
                dfs(r)
        return count

# improved solution 1 （卧槽这样改还就真能提高一点速度 220ms -> 160ms，如果知道数组的长度，就直接 [0]*len(M)吧，别append了。
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [0] * len(M)  # 改成一定长度
        count = 0

        def dfs(r):
            for c in range(len(M[0])):
                if visited[c] == 0 and M[r][c]: # 直接判断，不需要查找
                    visited[c] = 1
                    dfs(c)

        for r in range(len(M)):
            if visited[r] == 0:
                count += 1
                dfs(r)
        return count

# solution 2:
# 用queue，略

# 
"""


"""