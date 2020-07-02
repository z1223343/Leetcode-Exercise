"""
4 level solutions:
1. brute force
2. recursion with memoization
3. DP
4. DP with Binary Search

    time      space
2.  O(n**2)   O(n**2)
3.  O(n**2)   O(n)
4.  O(n*logn) O(n)
"""
# solution 3:
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(0, len(nums)):

            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)  # 注意哦，返回最大值，不是最后一个值

# solution 4: (真牛逼的思路，真巧，速度从 1000ms -> 30ms
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for i in range(0,len(nums)):
            index = bisect.bisect_left(dp,nums[i])
            if index == len(dp):
                dp.append(nums[i])
            else:
                dp[index] = nums[i]
        return len(dp)



# 课外拓展：
# 这个题下面这样写是不对的啊：(看似dp数组的len，只和dp数组中最大的一项的比较结果有关，天真的我写下了下面的代码
# 最典型的例子是[10000,10001,10002,1,2,3,4,5]
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = float('-inf')
        curr_secondmax = float('-inf') + 1
        n = 0
        for i in range(0, len(nums)):
            if nums[i] > curr_max:
                n += 1
                curr_secondmax = curr_max
                curr_max = nums[i]
            elif nums[i] > curr_secondmax:
                curr_max = nums[i]
        return n
