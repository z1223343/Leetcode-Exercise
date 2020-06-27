"""
2 level solution:
1. brute force (time exceed)
2. DP (caching)

    time   space
1.  O(n)    O(1)
2.  O(1)    O(n)
"""

# solution 2:
class NumArray:

    def __init__(self, nums: List[int]):
        self.sumlist = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.sumlist[i+1] = self.sumlist[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sumlist[j+1] - self.sumlist[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)