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

# 我想了半天想不明白，为什么下面这样写不行?????：老是超时 Time Limit Exceeded
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
From BFS to DFS: (总结的精辟啊)

In the above implementation of BFS, the fun part is that we could easily convert the BFS strategy to DFS by 
changing one single line of code. And the obtained DFS implementation is done in iteration, instead of recursion.

The key is that instead of using the queue data structure which follows the principle of FIFO (First-In First-Out), if 
we use the stack data structure which follows the principle of LIFO (Last-In First-Out), we then switch the strategy 
from BFS to DFS.

Specifically, at the moment we pop an element from the queue, instead of popping out the head element, we pop the tail 
element, which then changes the behavior of the container from queue to stack. Here is how it looks like.
"""