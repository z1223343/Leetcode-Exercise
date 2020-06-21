"""
1 solution:
1. Backtracking
time  O(N*4**L)   time  O(L)
"""

# 根据leetcode solution 我的原版: (runtime 在50%以下）
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = self.backtrack(board, i, j, word)
                if res:
                    return True
        return False

    def backtrack(self, board, r, c, suffix):
        if not suffix:
            return True

        if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0 or board[r][c] != suffix[0]:
            return False

        # res = False
        board[r][c] = '#'
        for nr, nc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            res = self.backtrack(board, r + nr, c + nc, suffix[1:])
            if res: break
        board[r][c] = suffix[0]

        return res

# 根据最快runtime的答案，偷学了一波：(把下面的代码放在function的最前面，runtime 可以提高到98%)
        n = len(board)
        m = len(board[0])
        if len(word)>n*m: return False

        #use dict to check whether number of char in the word is valid
        wordDict = {}
        for c in word:
            wordDict[c]=wordDict.get(c,0)+1

        for i in range(n):
            for j in range(m):
                if board[i][j] in wordDict:
                    wordDict[board[i][j]]-=1

        for k,v in wordDict.items():
            if v>0:
                return False #incorrect char number