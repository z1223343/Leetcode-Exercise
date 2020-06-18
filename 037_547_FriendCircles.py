"""
3 level solution:
1. DFS
2. BFS (用queue，和用stack很像)
3. Union Find

    time     space
1.  O(n**2)  O(n)
2.  O(n**2)  O(n)
3.  O(n**3)  O(n)  (谁叫你没用path compression)
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

# solution 3:
# 我看了，这个Union Find有点变种的意思啊，不是传统的。
# parents 默认设置成-1，find函数也是返回-1的下一层。
# 这个思路和DFS一比，也太绕了吧。 挺有意思。
# code略。
"""


"""