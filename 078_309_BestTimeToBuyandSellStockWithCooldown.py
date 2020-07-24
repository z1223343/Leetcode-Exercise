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

# solution 2