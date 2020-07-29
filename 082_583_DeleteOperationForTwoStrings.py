"""
1 level solution
1. 1D DP

     time    space
1.   O(m*n)  O(min(n,m))
"""

# 参考 problem 1143 求LCS 最长公共序列
# solution 1
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word,word2 = word2,word1
        rows = len(word1)
        cols = len(word2)
        dp_prev = [0]*(rows+1)
        dp_curr = [0]*(rows+1)
        for i in reversed(range(cols)):
            for j in reversed(range(rows)):
                if word1[j] == word2[i]:
                    dp_curr[j] = 1+dp_prev[j+1]
                else:
                    dp_curr[j] = max(dp_curr[j+1],dp_prev[j])
            dp_prev = dp_curr
            dp_curr = [0]*(rows+1)
        LCS = dp_prev[0]
        return rows+cols-2*LCS  # 和problem1143的唯一区别就是这里