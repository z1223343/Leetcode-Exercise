"""
3 level solutions
1. brute force (such a stupid way, but takes me long time to understand, the hard point is how to use 递归 或者说 DP (dynamics programming) to simulate the all (n**2)**n (still equal to n**n) possible cases of buy&sell stock.
2. Peak Valley Approach. 找左右的极大值和极小值，找的方法挺巧的，one pass 遍历就可以。
3. Simple One Pass. 终于来了个正常的思路。一步一步的走，只计算上坡的情况。

1. time O(n**n)  space O(n)
2. time O(n)  space O(1)
3. time O(n)  space O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(len(prices)-1):  # note should -1
            if prices[i] < prices[i+1]:
                maxprofit += prices[i+1] - prices[i]   # note +=
        return maxprofit