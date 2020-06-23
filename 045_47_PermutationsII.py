"""
1 solution
1. backtracking
"""
# solution 1: (github repo java solution rewrite in python)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def returnfalse():
            return False
        def backtrack(curr_list):
            if len(curr_list)==n:
                res.append(curr_list[:])
            else:
                for i in range(n):
                    if visited[i]:
                        continue
                    elif i!=0 and nums[i]==nums[i-1] and visited[i-1]!=0:
                        continue
                    visited[i] = True
                    curr_list.append(nums[i])
                    backtrack(curr_list)
                    curr_list.pop()
                    visited[i] = False
        res = []
        n = len(nums)
        visited = collections.defaultdict(returnfalse)
        backtrack([])
        return res


# improved version (90% time score)
class Solution(object):
    def permuteUnique(self, nums):
        def dfs(curr, nums):
            if (len(nums) == 0):  # conditions changed, watch out
                result.append(curr[:])

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:  # we dont create duplicate initial branches.
                    continue
                dfs(curr + [nums[i]], nums[:i] + nums[i + 1:]) # 简洁

        result = []
        nums.sort()
        dfs([], nums)  # sorted is sent
        return result




# 辣鸡算法 （time 大概是10%）
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def return_false():
            return False
        def backtrack(first=0):
            if first==n-1:
                if nums[:] not in visited:
                    res.append(nums[:])
                    visited.append(nums[:])
            else:
                for i in range(first,n):
                    nums[i],nums[first]=nums[first],nums[i]
                    backtrack(first+1)
                    nums[i],nums[first]=nums[first],nums[i]
        res = []
        visited = []
        n = len(nums)
        backtrack()
        return res
