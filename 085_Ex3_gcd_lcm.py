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