"""
2 level solution:
1. brute force (time exceeded)
2. binary search

   time space
1. N      1
2. logN   1
"""

# solution 2
# 我自己的解法：
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_left = bisect.bisect_left(nums,target)
        index_right = bisect.bisect_right(nums,target)
        if index_left == index_right:
            return [-1,-1]
        else:
            return [index_left,index_right-1]

# LeetCode Solution （我不明白为什么他手动写二分法，也是做了两次二分，为什么他submission运行时间快一点

class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums) # 这里看似是憨憨，这里平时都是len(nums)-1，见下面。这里是有意为之。

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target: # 这里是为了防止这个target非常大，二分法会把他判定在最后一位，而这里最后一位就不存在，所以可以返回[-1,-1]。 不对啊，这种情况也可以用num[left_idx}!=target判断啊，还是憨憨。不对，这时候nums[left_idx]
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
"""
About 'hi = len(nums)' and 'if left_idx == len(nums) or nums[left_idx] != target':
1.首先 hi = len(nums) 是有意为之，因为考虑到第二次用二分法求right index，我们的算法是上面写的这种，则当nums=[2,2] target=2时，
  right index会求错到1，你最后return的时候再-1就错了。所以我们索性把数组向后拓展一位，hi = len(nums)。
2.这样的话，会轻微影响到第一次用二分法，就是当如果target非常大，left_idx会把它放到len(nums)，而len(nums)不存在，所以后面的判断用
  'if left_idx == len(nums) or nums[left_idx] != target' 来判断。
  
二分法的这些细节真的还挺绕，有意思
"""