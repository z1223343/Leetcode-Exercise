"""
1 solution:
1. Backtracking

time  O(N!)
space  O(N)  ???不是O(N**2) 输出就是N**2 size
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(r, c):
            return not (cols[c] + hill_dia[r + c] + dale_dia[r - c])

        def place(r, c):
            queens.append([r, c])
            cols[c] = 1
            hill_dia[r + c] = 1  # 对角线这么解决 棒棒的
            dale_dia[r - c] = 1

        def remove(r, c):
            queens.pop()
            cols[c] = 0
            hill_dia[r + c] = 0
            dale_dia[r - c] = 0

        def add_solution():
            solution = []
            for _, c in queens:
                solution.append('.' * c + 'Q' + '.' * (n - c - 1))
            res.append(solution)

        def backtrack(r=0):
            for c in range(n):
                if could_place(r, c):
                    place(r, c)
                    if r + 1 == n:
                        add_solution()
                    else:
                        backtrack(r + 1)
                    remove(r, c)

        from collections import defaultdict
        res = []
        queens = []
        cols = defaultdict(int)
        hill_dia = defaultdict(int)
        dale_dia = defaultdict(int)
        backtrack()
        return res