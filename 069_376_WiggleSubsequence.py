"""


"""

# solution 4: 感觉greedy思路是更直接 靠近直觉的，但是code写起来并不直接

# solution 5: 自创版本
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        pre_diff = 0
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        ans = 2
        for i in range(1,len(nums)):
            diff = nums[i]-nums[i-1]
            if diff*pre_diff <0:
                ans += 1
            pre_diff = diff
        if ans == 2 and len(nums)>2:
            ans = 1
        return ans
