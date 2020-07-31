"""
使用未操作和减法求解最大公约数
1 level solution
"""

# solution 1:

def gcd(a: int ,b: int):
    if a<b:
        return gcd(b,a)
    if b == 0:
        return a

    if (a%2==0) and (b%2==0):
        return 2*gcd(a/2,b/2)
    elif (a%2==0) and (b%2!=0):
        return gcd(a/2,b)
    elif (a%2!=0) and (b%2==0):
        return gcd(a,b/2)
    else:
        return gcd(b,a-b)
"""
algorithm:

if both a and b are even, gcd(a,b) = 2*gcd(a/2,b/2)
if a is even while b is odd, gcd(a,b) = gcd(a/2,b)
if a is odd while b is even, gcd(a,b) = gcd(a,b/2)
if both a and b are odd, gcd(a,b) = f(b,a-b)

x2 and /2 can be done by Bit Operation
"""

# 其实感觉没上一题方法更接近真理，这个题是把2特殊化提取出来用位运算而已。哦？说不定位运算能加快算法time complexity