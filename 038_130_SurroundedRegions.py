"""
3 level solution:
1. DFS
2. BFS (DFS)

    time   space
1.  O(n)    O(n)
2.  O(n)    O(n)
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        from itertools import product
        border_cells = list(product(range(rows), [0, cols - 1])) + list(product([0, rows - 1], range(cols)))

        def dfs(r, c):
            if board[r][c] != 'O':
                return
            else:
                board[r][c] = 'E'
                if r < rows - 1:
                    dfs(r + 1, c)
                if r > 0:
                    dfs(r - 1, c)
                if c < cols - 1:
                    dfs(r, c + 1)
                if c > 0:
                    dfs(r, c - 1)

        for r, c in border_cells:
            dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
# 其实定义dfs函数，可以def dfs(self,board,r,c) 这样可以和solve function 并列，并且可以放在整个code的最后



# solution 2 (BFS)
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        from itertools import product
        border_cells = list(product(range(rows), [0, cols - 1])) + list(product([0, rows - 1], range(cols)))

        def bfs(r, c):
            if board[r][c] != 'O':
                return
            else:
                queue = []
                queue.append((r, c))
                while queue:
                    r, c = queue.pop(0)
                    if board[r][c] == 'O':
                        board[r][c] = 'E'
                        if r < rows - 1:
                            queue.append((r + 1, c))
                        if r > 0:
                            queue.append((r - 1, c))
                        if c < cols - 1:
                            queue.append((r, c + 1))
                        if c > 0:
                            queue.append((r, c - 1))

        for r, c in border_cells:
            bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'

# 我想了半天想不明白，为什么下面这样写不行?????：老是超时 Time Limit Exceeded： 我懂了！！！
                while queue:
                    r, c = queue.pop(0)
                    board[r][c] = 'E'
                    if r < rows - 1 and board[r + 1][c] == 'O':
                        queue.append((r + 1, c))
                    if r > 0 and board[r - 1][c] == 'O':
                        queue.append((r - 1, c))
                    if c < cols - 1 and board[r][c + 1] == 'O':
                        queue.append((r, c + 1))
                    if c > 0 and board[r][c - 1] == 'O':
                        queue.append((r, c - 1))
"""
这里解释一下：
这个超时的逻辑和正确答案的区别是： 这个超时的算法，检查出下一个等于0，才让它进队列，循环到这个值时才赋值其为E。而答案是把四个方向的下一
值都放进队列里，之后循环到它再判断是不是等于0，是0马上赋值为E。

我自己按照上两种逻辑自己画了个图，走了一遍，发现这个微小的逻辑区别会带来很大不用。总结就是我的超时逻辑会让一些点重复进队列，重复产生新的
四个点，而且这个重复会累计起来，增长速度可比指数。当一个矩阵很大而且多为0时，就会超时。

这里演示一下：
设题目为：
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 
0 0 0 0 0 

按我的超时逻辑，会这样：（数字代表这个位置的值进入队列和被判断是否为0的次数）
1  1  1  1  1
1  2  3  4  5
1  3  6  10 15
1  4  10 20 35
1  5  15 35 70

正确答案是这样：

1  1  1  1  1
1  2  2  2  2 
1  2  2  2  2
1  2  2  2  2
1  2  2  2  2
最多就是2了，以为第一次判断就 把其赋值为E，第二次因此不等于0，不会再把这个重复传递给后一级
"""

# 对于以上问题进行优化，下面是我认为的最屌算法：
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        from itertools import product
        border_cells = list(product(range(rows), [0, cols - 1])) + list(product([0, rows - 1], range(cols)))

        def bfs(r, c):
            if board[r][c] != 'O':
                return
            else:
                board[r][c] = 'E'
                queue = []
                queue.append((r, c))
                while queue:
                    r, c = queue.pop(0)
                    if r < rows - 1 and board[r + 1][c] == 'O':
                        board[r+1][c] = 'E'
                        queue.append((r + 1, c))
                    if r > 0 and board[r - 1][c] == 'O':
                        board[r-1][c] = 'E'
                        queue.append((r - 1, c))
                    if c < cols - 1 and board[r][c + 1] == 'O':
                        board[r][c+1] = 'E'
                        queue.append((r, c + 1))
                    if c > 0 and board[r][c - 1] == 'O':
                        board[r][c-1] = 'E'
                        queue.append((r, c - 1))
        for r, c in border_cells:
            bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
"""
这个的次数应该是
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
但要注意啊，这个四个方向拓展的DFS本身就要把一些值 重复判断，这个没办法
"""



"""
From BFS to DFS: (总结的精辟啊)

In the above implementation of BFS, the fun part is that we could easily convert the BFS strategy to DFS by 
changing one single line of code. And the obtained DFS implementation is done in iteration, instead of recursion.

The key is that instead of using the queue data structure which follows the principle of FIFO (First-In First-Out), if 
we use the stack data structure which follows the principle of LIFO (Last-In First-Out), we then switch the strategy 
from BFS to DFS.

Specifically, at the moment we pop an element from the queue, instead of popping out the head element, we pop the tail 
element, which then changes the behavior of the container from queue to stack. Here is how it looks like.
"""