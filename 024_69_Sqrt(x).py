# 二分查找 专题开始
"""
3 solution:
1. Pocket Calculator Algorithm. Although may not be used in interviews, it's interesting and can learn something.
2. Binary Search. 标准的二分算法
3. Recursion + Bit Shifts 牛逼的新颖算法，转大问题为基本问题。
4. Newton's Method

   time    space
1. O(1)  O(1)
2. O(logN) O(1)
3. O(logN) O(1)
4. O(logN) O(1)
"""
# solution 1:
from math import e, log
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left = int(e ** (0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right
"""
1. 为啥用e,log 而不直接用sqrt开方呢。 因为工程实际中，计算器善于exponential functions & natural logarithms，by having log
   table hardcoded or other means.
2. 为啥还要分left right. 用right=left+1 来检测呢，因为以4为input为例，int(e**(0.5*log(4))算出的是1.999999999999998而不是2，
   这时候就要用right来解决这个特殊问题
"""
# ================================================
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

# ================================================
# solution 3
# 刚看懂时：卧槽这思路牛逼。 仔细想了半个小时又动手试了一些例子：卧槽这太牛逼了。
# 症结: 我现在也没完全想明白怎么证明这个算法对所有整数都可以得出正确答案。我指这个left right机制，以及什么时候用到right
#      这里应该对 取整的影响有深刻的理解，sqrt的结果取了整，/4结果也取了整。/4只影响前期，主要是sqrt取整的问题，为什么+1呢，因为每次
#      sqrt*2，但有时候需要sqrt*2+1，因为前一个sqrt是不准的，是被阉割的。
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = self.mySqrt(x>>2)<<1
        right = left+1
        return left if right*right>x else right
"""
1. 位运算，python也可以。 >>n means /2**n , <<n means *2**n, 而且这里位运算的结果返回一个整数int 
2. left right 机制。
3. 我感觉solution分析的complexity有点问题啊，根据master theorem不应该是a=1 b=1/4 d=0 吗？
"""

#===================================================
# solution 4
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2

        return int(x1)
"""
我尼玛回味了大名鼎鼎的牛顿法：https://blog.csdn.net/ccnt_2012/article/details/81837154
想明白我们要求根的等式是 x**2-k=0


症结是这个最后的error 设为>=1的时候停止，你告诉我为什么。我知道开始从x0=x，必然是在大的那一端。但你怎么知道和下一个值差距1以内，
你就知道下一值和真正的根落在同一个整数上。？？？

最后LeetCode submit Time Limit Exceeded又是咋回事
"""
