"""
1 level solution:
1. math
"""

# solution 1:
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        res = ""
        if num<0:
            num+=1<<32  # 不是很明白 为什么+2**31 就是补码了
        while num != 0:
            last = num%16
            if last<10:
                res = str(last) + res
            else:
                res = chr(last-10+ord('a')) + res
            num //= 16
        return res

