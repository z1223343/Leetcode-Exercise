# 今日忙opt extension
# 此题开始 注意提速

"""
3 solutions
1. Divide and Conquer
2. Greedy
3. DP
(算法分析见下面）

     time      space
1.  O(NlogN)  O(logN)
2.  O(N)      O(1)
3.  O(N)      O(1)
"""
# 1. Divide and Conquer
# 这种思路的确很巧妙，但是和greedy比起来太难想，也太复杂了。怎么解释这种方法是可行的呢？这么理解：它其实是想找一个点，只要这
# 点在我们要的maximum subarray里面，就可以用get cross_sum的算法找到这个subarray。那怎么找这个点呢？二分法的方式找。

# Solution Complexity 部分学了一手主定理(Master Theorem)
#============================================
# 2. Greedy Algorithm
# 自己写的
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_curr = float('-inf')
        max_global = float('-inf')

        for n in nums:
            if n > n + max_curr:
                max_curr = n
            else:
                max_curr = n + max_curr
            if max_curr > max_global:
                max_global = max_curr
        return max_global
# 果然LeetCode solution写的更简洁
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum
#=============================================
# Dynamic Programming
# 算法上和greedy很相似，是用另一个角度（DP的角度）思考这个问题。