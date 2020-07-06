"""
3 level solutions:
1. memoization
2.

   time       space
1. O(M*N**2)  O(M*N)
2.
3.
"""

# solution 1: (copy leetcode solution)
from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):

            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Option 1: We don't include text1[p1] in the solution.
            option_1 = memo_solve(p1 + 1, p2)

            # Option 2: We include text1[p1] in the solution, as long as
            # a match for it in text2 at or after p2 exists.
            first_occurence = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurence != -1:
                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)

            # Return the best option.
            return max(option_1, option_2)

        return memo_solve(0, 0)
"""
from functools import lru_cache 
@lru_cache(maxsize=None)
def memo_solve(p1,p2):
    ...
这个装饰器厉害啊，可以缓存函数结果：
https://blog.csdn.net/u012745215/article/details/78506022
"""


"""
solution essay 解释了如何看待dp和greedy两种算法，什么时候应该怎么想的问题，挺好的
这个文章我看的很仔细，各个级别的算法思路和intuition我都看了，可以当做一个DP教学.
"""