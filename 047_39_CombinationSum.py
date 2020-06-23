"""
1 solution:
1. Backtracking

"""

# solution 1. time score: 34%. 有待改进速度，这里先不想了。
class Solution(object):
    def combinationSum(self, candidates, target):
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
                curr.append(candidates[i])
                backtrack(i,curr)
                curr.pop()
        res = []
        backtrack()
        return res



"""
我一步一步debug看了看，发现重复变量（传引用）只影响同级（和下级）循环的这个重复变量，上级的这个同名变量还是原来当时的值。
以上是放屁，请忽略。上级也影响。
"""

# 粘贴discussion别人的solution写法。 一样的time score.
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        self.res, self.target = [], target
        self.dfs(candidates, [], 0)
        return self.res

    def dfs(self, nums, current, start):
        if sum(current) == self.target:  # Base case, if the current numbers sum upto the target
            self.res.append(current)  # Appending to the result array
            return
        if sum(current) > self.target:  # optimization
            return
        for i in range(start, len(nums)):
            self.dfs(nums, current + [nums[i]], i)  # not i + 1 because we can reuse the same number  # yaozhong: 这个写法就太骚了，在挑战函数传参的极限啊。