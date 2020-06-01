"""
1 solution:
1. single scan

time O(N)  space O(1)
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            if (i==0 or flowerbed[i-1]==0) and (flowerbed[i]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):  # Note that i==len(flowerbed)-1, dont forget -1
                flowerbed[i] = 1
                count += 1
            if count >= n:   # Note that == does not work, when the question has n = 0, and we gonna have a count start from 1
                return True
        return False


"""
In python, 逻辑运算符and 和or, 为惰性求值：
python中的逻辑操作符and 和or，也叫惰性求值，就是从左至右解析，由于是惰性，只要确定了值就不往后解析代码了
or 或者，只要第一个是True或非0，整条指令为True或非0。反之，如果第一个是True，后面不管是True还是False，都是后面结果。
and 并且，只要第一个是False，就是False，后面的就不需要运算了，整个都是错误的，无论后面是正确还是错误。反之，第一个是True，
直接返回后面的值，意思就是两个为True，整个句子为True，有一个为False，整个都是False。
"""