"""
1 level solution:
1. DP
"""

# solution 1
# “涉及顺序的完全背包问题"
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        maximum = [0]*(target+1)
        maximum[0] = 1
        #nums.sort()
        for i in range(1,target+1):
            for j in range(0,len(nums)):
                if nums[j]<=i:
                    maximum[i] += maximum[i-nums[j]]
        return maximum[target]