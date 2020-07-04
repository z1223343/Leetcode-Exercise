"""


"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        up = [0]*len(nums)
        down = [0]*len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    up[i] = max(up[i],down[j]+1)
                elif nums[i]<nums[j]:
                    down[i] = max(down[i],up[j]+1)
# solution 4: 感觉greedy思路是更直接 靠近直觉的，但是code写起来并不直接
# 是牛逼的，我想了半天，为什么看似相似的算法，答案就没有像我的算法一样被边界情况所困扰，为什么它能接受0的存在，算法思想是博大精深的
# 答案的思路好像也是找拐点，但是 if (diff>0 and prevdiff<=0) or (diff<0 and prevdiff>=0) 保证了进入循环后prevdiff再也不可能为0
# 这个prediff=0就是为了initial时prediff可能等于0准备的，然后 count = 2 if prevdiff!=0 else 1 这一步补偿。这一步也神奇的解决了一个“拐点”也没有时，有1有0的情况。
# 感觉有改进的空间啊，我想了十几分钟，没想出什么好方案。
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        prevdiff = nums[1]-nums[0]
        count = 2 if prevdiff!=0 else 1
        for i in range(2,len(nums)):
            diff = nums[i] - nums[i-1]
            if (diff>0 and prevdiff<=0) or (diff<0 and prevdiff>=0):
                count += 1
                prevdiff = diff
        return count


# solution 5: 自创版本 （卧槽，算法还挺快的
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
            if diff == 0:
                continue
            pre_diff = diff
        if ans == 2 and len(nums)>2:
            if min(nums) == max(nums):
                return 1
        return ans
# 这个算法不太好，因为这个算法实际上是找‘拐点’，但题目问的是构成wiggle的元素数量，在一个拐点也没有时，答案有时为0有时为1,还要用额外的code去区分这个点。
