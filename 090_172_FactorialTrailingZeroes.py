"""
1 level solution:
1. math

time: O(logN)   space：O(1)
"""
# 通过数学分析一下，答案等于N//5 + N//5**2 + N//5**3

# solution 1
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero=0
        current_power = 5
        while n>=current_power:
            zero += n//current_power
            current_power*=5
        return zero




# solution 1 另一种写法，time&space complexity 相同：
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero = 0
        while n>0:
            n//=5
            zero += n
        return zero
# code精简的令人发指...