"""
1 solution:
1. bracktracking
"""
# solution 1 (第一次如此流畅地写出一个没有Bug的代码，而且time score 90% 以上)
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtrack(first,curr,n):
            if len(curr)==k:
                if n==0:
                    res.append(curr[:])
            else:
                for i in range(first,10):
                    if i>n:
                        break
                    curr.append(i)
                    backtrack(i+1,curr,n-i)
                    curr.pop()
        res = []
        backtrack(1,[],n)
        return res