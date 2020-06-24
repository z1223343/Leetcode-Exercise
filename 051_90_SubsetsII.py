"""
1 solution:
1. Backtracking
"""
# solution 1. （轻松且愉快
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first,curr):
            for i in range(first,len(nums)):
                if i==first or nums[i]!=nums[i-1]:
                    curr.append(nums[i])
                    res.append(curr[:])
                    backtrack(i+1,curr)
                    curr.pop()
        nums.sort()
        res = [[]]
        backtrack(0,[])
        return res