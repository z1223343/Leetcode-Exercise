"""
3 level solutions:
1. memoization
2.

   time       space
1. O(M*N**2)  O(M*N)
2. O(M*N)     O(M*N)
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
.find()用法：(使用的数据类型是str,list啥的不行)
str.find(str, beg=0, end=len(string))
检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内包含指定索引值，则返回索引值在字符串中的起始位置，否则返回-1

example:
a = '1234523456'
print(a.find('2'))
print(a.find('2',1))
print(a.find('2',2))
ans:
1
1
5
"""

# solution 2: (这可以归为传说中的双指针吗)(这个比上面的solution 1更接近我的自然思路一点)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        from functools import lru_cache
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))

        return memo_solve(0, 0)

# solution 3: (好好想想谁是row,谁是col,长度又分别是多少)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        rows = len(text1)
        cols = len(text2)
        dp = [[0] * (cols + 1) for i in range(rows + 1)]

        for i in reversed(range(cols)):
            for j in reversed(range(rows)):
                if text1[j] == text2[i]:
                    dp[j][i] = 1 + dp[j + 1][i + 1]
                else:
                    dp[j][i] = max(dp[j + 1][i], dp[j][i + 1])
        return dp[0][0]

# solution 4: (好好想想，为了节省空间，text1 text2谁应该更短; 循环的时候是循环的是行还是列，这是一个哲学问题lol，行数是len(text1)还是text1本身
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text1) > len(text2):
            text1, text2 = text2, text1
        rows = len(text1)
        cols = len(text2)
        dp_prev = [0] * (cols + 1)
        dp_curr = [0] * (cols + 1)

        for i in reversed(range(cols)):
            for j in reversed(range(rows)):
                if text1[j] == text2[i]:
                    dp_curr[j] = 1 + dp_prev[j + 1]
                else:
                    dp_curr[j] = max(dp_curr[j + 1], dp_prev[j])
            dp_prev = dp_curr
            dp_curr = [0] * (cols + 1)
        return dp_prev[0]

# solution 4 (a little bit improved by reusing the reference of dp_prev, at the end of loop)(according to LeetCode solution)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        # The previous and current column starts with all 0's and like
        # before is 1 more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)

        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one, and vice versa.
            previous, current = current, previous

        # The original problem's answer is in previous[0]. Return it.
        return previous[0]


"""
solution essay 解释了如何看待dp和greedy两种算法，什么时候应该怎么想的问题，挺好的
这个文章我看的很仔细，各个级别的算法思路和intuition我都看了，可以当做一个DP教学.
"""