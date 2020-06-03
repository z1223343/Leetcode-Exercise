


# my first idea
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curr = 0
        chance = 1

        while curr < len(nums) - 1:
            if nums[curr] > nums[curr + 1]:
                if (curr - 1 < 0):
                    curr += 1
                elif (nums[curr - 1] > nums[curr + 1]):
                    if (curr + 2 < len(nums)) and nums[curr] > nums[curr + 2]:
                        return False
                    curr += 2
                else:
                    curr += 1
                chance -= 1
            else:
                curr += 1
            if chance < 0:
                return False
        return True

# my second trial. Why slower than the first one?? LeetCode processing time is not accurate?
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curr = 0
        chance = 1

        while curr < len(nums) - 1:
            if nums[curr] > nums[curr + 1]:
                if (curr - 1 >= 0) and (nums[curr - 1] > nums[curr + 1]):
                    nums[curr + 1] = nums[curr]
                chance -= 1
            curr += 1
            if chance < 0:
                return False
        return True