"""
The two questions are actually one problem. Same Code.

3 level solution (but we only focus on DP)

1. Recursion
2. DP
3. Formula

    time  space
1. O(n)   O(n)
2. O(n)   O(1)
3. O(n)   O(1)
"""

class Solution:
    def findDerangement(self, n: int) -> int:
        if n==1:
            return 0
        if n==2:
            return 1
        pre1 = 1
        pre2 = 0
        for i in range(3,n+1): # 注意这里是n+1，
            curr = ((i-1)*pre1 + (i-1)*pre2) % 1000000007 # 题目要求 mod 10**9+7, 就是这个意思
            pre2 = pre1
            pre1 = curr
        return curr

"""
关于信件错排题目描述已经分析：
https://blog.csdn.net/qq_40320556/article/details/89785464
"""