"""
1 solution:
1. Backtracking
"""
# solution 1. (time score 80%
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def backtrack(first,curr):
            if first == len(s):
                res.append(curr[:])
            else:
                for i in range(first,len(s)):
                    if isPal(s[first:i+1]):
                        curr.append(s[first:i+1])
                        backtrack(i+1,curr)
                        curr.pop()
        def isPal(s):
            return s == s[::-1]
        res = []
        backtrack(0,[])
        return res

# 原答案：https://blog.csdn.net/danspace1/article/details/88084384