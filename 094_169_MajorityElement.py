"""
2 level solution:
1. sort and get median (略)
2. Boyer-Moore Majority Vote Algorithm (一个神奇的算法)

    time      space
1.  O(NlogN)  O(1)
2.  O(N)      O(1)
"""

# solution 2 (my version，和下面leetcode solution code写法在顺序上稍有不同，但都通过了测试)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = nums[0]
        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = num
                count = 1
        return candidate

# solution 2 (from leetcode solution)
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate