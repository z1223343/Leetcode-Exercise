"""
2 level solutions:
1. Backtracking
2. Lexicographic (binary sorted) combinations

     time         space
1. O(k* C^k_N)   O(C^k_N)
2. O(k* C^k_N)   O(C^k_N)
"""

# solution 1
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(first=1,curr=[]):
            if len(curr) == k:
                res.append(curr[:])
            else:
                for i in range(first,n+1):
                    curr.append(i)
                    backtrack(i+1,curr) # 注意是i+1,才保证了组合
                    curr.pop()
        res = []
        backtrack()
        return res

# solution 2
# 还没看