"""
4 level solution
1. brute force (愚蠢的暴力美学，能写出来也不容易的）
2. Reduce to Smaller Problem (想法可以的，我边跑步边想明白了，有点是分而治之（大事化小）的思想啊，但最后还是要借用brute force，那这要写多少代码啊）
3. Locate and Analyze Problem Index (这解法算哪个派系的？感觉就是针对这一题的，反正不是greedy）
4. 自己的解法 （有greedy的一点意思）

   time    space
1. O(N)    O(N)
2. O(N)    O(1)
3. O(N)    O(1)
4. O(N)    O(1)
"""


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

# LeetCode Solution 挺亮眼的，不一样的角度。但这和greedy没有鸡毛关系了吧
class Solution(object):
    def checkPossibility(self, A):
        p = None
        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(A)-2 or
                A[p-1] <= A[p+1] or A[p] <= A[p+2])

"""
自己探索出来的解法，牛逼的。算是用了greedy的思想
而且我的还适用于‘可以改n个数’的题目变形
"""