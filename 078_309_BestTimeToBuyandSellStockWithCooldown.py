"""
1 level solution:
1. DP (with state machine)

    time   space
1.  O(N)    O(1)
"""

# soulution 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = float('-inf')
        held = float('-inf')
        reset = 0
        for price in prices:
            pre_sold = sold
            sold = held + price
            held = max(held,reset-price)
            reset = max(reset,pre_sold)
        return max(sold,reset)

# solution 1 改 （用下一题的思路写的）其实两种思路是一样的。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        held = float('-inf')
        rest = 0
        cash = float('-inf')
        for price in prices:
            cash, held, rest = held+price, max(held,rest-price), max(cash,rest)
        return max(cash,rest)