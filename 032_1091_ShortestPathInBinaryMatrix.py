"""
1 level solution：
1. BFS (广度优先搜索)

time: O(N**2)  space: O(N**2)
"""


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        # eight directions
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # 里面是元组tuple还是列表list都可以

        queue = [(0, 0, 1)]
        n = len(grid)

        while queue:
            x, y, cnt = queue.pop(0)  # 注意删除的是第一个！
            if x == n - 1 and y == n - 1:
                return cnt
            for i, j in directions:
                x1, y1 = x + i, y + j
                if 0 <= x1 < n and 0 <= y1 < n and grid[x1][y1] == 0:  # Note 0<=0
                    queue.append((x1, y1, cnt + 1))
                    grid[x1][y1] = 1  # 这里是巧妙的
        return -1

"""
问最短路径就上BFS. 但必须是求解无权图的最短路径，无权图是指从一个节点到另一个节点的代价都记为 1

模板：
void BFS(){
    判断边界条件，是否能直接返回结果的。
    
    定义队列；
    定义备忘录，用于记录已经访问的位置；

    将起始位置加入到队列中，同时更新备忘录。

    while (队列不为空){
        获取当前队列中的元素个数。
        判断是否到达终点位置。
        
        for (元素个数){
            取出一个位置节点。
            判断是否到达终点位置。
            获取它对应的下一个所有的节点。
            条件判断，过滤掉不符合条件的位置。
            新位置重新加入队列。
        }
    }
}

https://blog.csdn.net/Wonz5130/article/details/104525673
"""