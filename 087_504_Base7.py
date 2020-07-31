"""
1 level solution:
1. math (using % // )
"""

# solution 1:
# https://blog.csdn.net/fuxuemingzhu/article/details/70194688
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []
        sign = num>0
        num = abs(num)
        while num!=0:
            res.append(num%7)
            num //= 7
        return ("" if sign else "-") + "".join(map(str,res[::-1]))

# 注意map的用法， map(func,iterable,..)
# 这个函数的意思就是将function应用于iterable的每一个元素，结果以列表的形式返回。 https://blog.csdn.net/csdn15698845876/article/details/73321593


# 注意啊 -12%5 得 3。 很神奇但也好理解，这样说明我们要单独判断符号了。