"""
1 solution:
1. Backtracking
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(first=0,curr=[]):
            if sum(curr) == target:
                res.append(curr[:])
                return
            if sum(curr) > target:
                return
            for i in range(first,len(candidates)):
                if candidates[i] == candidates[i-1] and i-1>=first: # 我差点儿自己都不知道为什么自己写的code可行
                    continue
                curr.append(candidates[i])
                backtrack(i+1,curr)
                curr.pop()
        candidates.sort()
        res = []
        backtrack()
        return res