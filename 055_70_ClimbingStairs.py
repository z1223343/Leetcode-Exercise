"""
6 level solutions:
1. brute force
2. recursion with memoization
3. Dynamic Programming
4. Fibonacci Number
5. Binets Method
6. Fibonacci Formula

    time      space
1.  O(2**n)   O(n)
2.  O(n)      O(n)
3.  O(n)      O(1) (我这个算法不keep all dp[i], 所以是O(1), 而不是O(n), 我这个code更像leetcode的 solution 4
4.  O(n)      O(1)
5.  O(logn)   O(1)
6.  O(logn)   O(1)
"""

# solution 3 (DP)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp_pre1 = 2
        dp_pre2 = 1
        for i in range(3,n+1):
            curr = dp_pre1+dp_pre2
            dp_pre2 = dp_pre1
            dp_pre1 = curr
        return curr