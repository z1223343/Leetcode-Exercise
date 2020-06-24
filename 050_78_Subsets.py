"""
3 level solutions:

1. Cascading
2. Backtracking
3. Lexicographic (Binary Sorted) Subsets

    time      space
1. O(N*2**N)  O(N*2**N)
2. O(N*2**N)  O(N*2**N)
3. O(N*2**N)  O(N*2**N)
"""
# solution 2: (没有难度好吗) 我这个应该还比答案牛逼
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first,curr):
            for i in range(first,len(nums)):
                curr.append(nums[i])
                res.append(curr[:])
                backtrack(i+1,curr)
                curr.pop()
        res = [[]]
        backtrack(0,[])
        return res