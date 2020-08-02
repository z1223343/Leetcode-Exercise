"""
2 level solution:
1.Left and Right product lists (without space optimization)
2.Left and Right product lists (with space optimization)

      time   space
1.    O(n)   O(n)
2.    O(n)   O(1)
"""

# solution 1:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        L = [0]*n
        R = [0]*n
        L[0] = 1
        for i in range(1,n):
            L[i] = L[i-1]*nums[i-1]
        R[n-1] = 1
        for i in range(n-2,-1,-1):
            R[i] = R[i+1]*nums[i+1]
        for i in range(n):  # range别搞错了
            ans[i] = L[i]*R[i]
        return ans

# solution 2：（算的我晕了吧唧的）
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        ans[0] = 1
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        tmp = 1
        for i in range(n - 2, -1, -1):
            tmp = nums[i + 1] * tmp
            ans[i] = ans[i] * tmp

        return ans