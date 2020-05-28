"""
2 ideas of solutions:
1. count sort (by myself, two pass)
2. one pass (三向切分快速排序?)

1.
2. time O(N)  space O(1)
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        countlist = [0 for i in range(3)]
        for element in nums:
            if element == 0:
                countlist[0] += 1
            elif element == 1:
                countlist[1] += 1
            else:
                countlist[2] += 1

        curr = 0
        for i, num in enumerate(countlist):
            for j in range(num):
                nums[curr] = i       # 就狠蛋疼，这里这样用指针遍历一个一个值改nums才行，如果重设nums = 0,然后用nums.append(i)，
                                     # 结果错误，nums 还是等于初始值。 python似乎重设nums的话实际上重新定义了一个新变量。
                curr += 1




class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0
        p2 = len(nums) - 1

        while curr <= p2:  # 想明白了，这里有等于
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1        # Note curr have no change
            else:
                curr += 1
