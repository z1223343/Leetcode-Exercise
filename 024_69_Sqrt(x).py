# 二分查找 专题开始
"""


"""
# solution 2:
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:
            return x
        l = 1
        h = x-1
        while l<=h:
            m = l + (h-l)/2
            sqrt = x / m
            if sqrt == m:
                return sqrt
            elif sqrt < m:
                h = m-1
            else:
                l = m+1
        return h
# 算法之美，一个很简单的问题，想透彻并不容易，要考虑所有可能的情况。

# LeetCode solution: improve by reducing the range to 2 - x//2
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot

        return right