"""
2 level solution:
1. brute force: delete every element in list and check if the rest is palindrome.
2. Two pointers (greedy): use two points traversing from head and tail. If different, delete it and check if the rest sub-list is palindrome. Note there are two cases of deleting.

1. Time:O(N**2) Space:O(N)
2. Time:O(N) Space:O(1)
"""

# my answer:
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def is_pali_range(a, b):
            while a < b:
                if s[a] == s[b]:
                    a += 1
                    b -= 1
                else:
                    return False
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # delete s[i] or s[j]
                x = is_pali_range(i + 1, j)
                y = is_pali_range(i, j - 1)
                return x | y
        return True




# LeetCode solution: (有点反应不过来）
class Solution(object):
    def validPalindrome(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))       # 我又看傻了，这是个遍历，此ij非彼ij.

        for i in xrange(len(s) / 2):
            if s[i] != s[~i]:         # 我看傻了 ~按位取反
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True




"""
In python:

range -> 生成一个list
range(5): [0,1,2,3,4,5]
range(1,5): [1,2,3,4,5]
range(0,6,2): [0,2,4]

xrange -> 用法与range完全相同，不同的是生成的不是一个list，而是一个生成器
xrange(5): xrange(5)
list(xrange(5)): [0,1,2,3,4,5]

由上面的示例可以知道：要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间，这两个基本上都是在循环的时候用
for i in range(0,100) 和 for i in xrange(0,100) 效果完全一样。
"""

"""
a[::-1] 倒序
a[:i] 不包括 a[i]
所以捏，t = a[:i] + a[i+1:]： t代表a删掉a[i]的新list
"""

# python 子函数要在被调用前定义，被同级函数调用除外
# all() 全真为真 any() 全假为假


# Python 中 （&，|）和（and，or）之间的区别: https://blog.csdn.net/weixin_40041218/article/details/80868521

"""
~ 位运算符： ~5 = -6
https://blog.csdn.net/lanchunhui/article/details/51746477
"""