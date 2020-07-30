"""
1 level solution:

1. 额，玩数学的，作为DP最后一题，这里我没有用DP

time: O(n**0.5)   space: O(1)
"""
# solution 1 (from LeetCode solution)
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n>1:
            while n%d == 0:
                ans += d
                n /= d
            d+=1
        return ans

# 挺巧妙好玩的，用纸笔写写