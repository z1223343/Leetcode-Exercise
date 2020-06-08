"""
1 level solution (其实brutal force肯定也可以啊）

1. binary search (此题为非常标准的binary search problem，而且和上一题的code非常非常相似，但是这个题的特殊情况太恶心了，增加了一些特殊情况的判断。

time O(logN)  space O(1)
"""
# 自己写的，没看leetCode答案，不知道他是啥思路，感觉自己很帅。
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        l = 0
        h = len(nums)-1
        while l<h:
            mid = l+(h-l)//2
            if nums[0]<=nums[mid]:
                l = mid+1
            elif nums[0]>nums[mid]:
                h = mid
        if (l==len(nums)-1) and (nums[-1]>nums[-2]):
            return nums[0]
        else:
            return nums[l]