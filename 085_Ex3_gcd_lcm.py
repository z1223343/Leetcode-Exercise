"""
GCD: Greatest Common Divisor
LCM: Least Common Multiple
"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return a*b / gcd(a,b)
# 最小公倍数为两数的乘积除以最大公约数

# 汝甚骚..

# 额我应该是想明白了，没毛病。 两个数都是最大公约数乘以某个数，我们只要把那个数折磨减小至1，则剩下的就是gcd

# 有一个事是，a%b 肯定小于等于b，所以(b,a%b). 而后面一题用减法，因此最好判断一下b，a-b谁大（在函数最前面）