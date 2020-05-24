"""
the difference between this one and problem 1 'TwoSum' is that:
in this problem, the input list is ordered.

So, further updated from the level3 in problem 1, in this problem we can use 'two pointers'
which can reduce space complexity to O(1) and keep time as O(n)
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1



"""
In python, no matter dict or list, use [] for index, e.g. a[1]=b

In python, if, elif, else

In python, do not use sum()

In python, return([a,b])  return [a,b]  both work
"""

"""
Two points 

such a magic way to deal with this kind of problem: 
In a sorted list find a sum of two elements to satisfy a requirement.
But the drawback is only being able to find one answer?

"""