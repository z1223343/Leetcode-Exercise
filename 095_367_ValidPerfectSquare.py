"""
2 level solution:
1. elementary math
2. Newton's method

    time    space

"""

# solution 1 (from github guideline)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        subnum = 1
        while num>0:
            num-=subnum
            subnum += 2
        return num == 0

# solution 2 (from Leetcode solution)
# 我打通了牛顿法，牛顿法无敌了。
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<2:
            return True
        x = num//2
        while x*x>num:
            x = (x+num//x)//2
        return (x*x == num)
# 但我这里还是不明白为什么 用//整除就能用来判断出valid perfect square