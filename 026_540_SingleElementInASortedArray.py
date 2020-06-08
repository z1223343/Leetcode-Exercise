"""
1. brute force (挨个找 下一个元素和自己一不一样 range(0,len(nums)-2,2)
2. Binary Search
3. Binary Search on Evens indexes only

   time  space
1.  N     1
2. logN   1
3. log(N/2)=logN  1
"""

# solution 2
# 这个解法就是要把4种情况想清楚，在图上画明白，看图说话
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        while l<h:
            mid = l+(h-l)//2
            halves_are_even = (h-mid)%2==0 #注意是%啊
            if nums[mid]==nums[mid+1]:
                if halves_are_even:
                    l = mid+2
                else:
                    h = mid-1
            elif nums[mid]==nums[mid-1]:
                if halves_are_even:
                    h = mid-2
                else:
                    l = mid+1
            else:
                return nums[mid]
        return nums[l]

# solution 同样是 binary search，但这个感觉思想更自然一些（从基本的binary search改版），“more elegent".
# 这个情况也少，不需要看图说话，喜欢这个。
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        while l<h:
            mid = l+(h-l)//2
            if mid%2 == 1:
                mid-=1
            if nums[mid] == nums[mid+1]:
                l = mid+2
            else:
                h = mid
        return nums[l]