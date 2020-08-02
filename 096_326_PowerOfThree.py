"""
2 level solutions:
1. Loop iteration (正常做法）
2. Interger limitation （牛逼做法）

    time       space
1. O(log3(n))  O(1)
2.  O(1)       O(1)
"""
# solution 1:
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        while n%3 == 0:
            n/=3
        return n==1


# solution 2:
import math
maxint = 2**32/2-1
maxpower = int(math.floor(math.log(maxint,3)))
maxpowerof3 = 3**maxpower
print(maxint,maxpower,maxpowerof3)

# maxpowerof3 = 1162261467
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return (n>0) and (1162261467%n==0)