"""
1 level solution:
1. DP

    time    space
1.  O(N)    O(1)
"""
# 1 solution:
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, float('-inf')
        for price in prices:
            cash = max(cash,hold+price-fee)
            hold = max(hold,cash-price)
        return cash

"""
短短五行代码，leetcode solution也就两句话。
但是其中的道理让人想很长时间，solution分析是对的，思路也很简单，但是它为什么在任何情况下都行的通呢，为什么这么简单就
囊括了题目条件 （必须一次持有一次股票，并且有transaction fee，也没说具体买入卖出怎么分担这个fee.）
牛逼
罗列下基本所有的代表情况，这循环里的两行代码都能用数学正确的解出来，可见这个DP的思路是简单
又可行的

更好玩的是这个代码里对待股票的思路和我的直觉也有不同，不过after all这里的股票和真实的股票买卖也有很大区别
"""