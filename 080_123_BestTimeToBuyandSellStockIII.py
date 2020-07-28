"""
2 level solutions:
1. Bidirectional Dynamic Programming
2. One-pass Simulation

     time   space
1.   O(N)    O(N)
2.   O(N)    O(1)
"""

# solution 1:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        length = len(prices)
        left_min = prices[0]
        right_max = prices[-1]
        left_profits = [0] * length
        right_profits = [0] * (length + 1)
        max_profit = 0

        for l in range(1, length):
            left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - 1 - l
            right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        for i in range(0, length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])
        return max_profit

# solution 2:
# 真牛逼，我服了
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float('inf'),float('inf')
        t1_profit, t2_profit = 0,0
        for price in prices:
            t1_cost = min(t1_cost,price)
            t1_profit = max(t1_profit,price-t1_cost)
            t2_cost = min(t2_cost,price-t1_profit)
            t2_profit = max(t2_profit,price-t2_cost)
        return t2_profit