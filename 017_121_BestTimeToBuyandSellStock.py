"""
2 level solution:
1. brute force (too stupid)
2. one pass (I don't think it is literally Greedy Algorithm, cuz it is not compliant with the Greedy definition before

1. time O(n**2) space O(1)
2. time O(n)    space O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = None
        maxprofit = 0
        for p in prices:
            if (minprice==None) or (p < minprice):   # 我真吐了，这里不能用(not miniprice)，因为后面miniprice会为0，这里是想检测是否为None,0也会判定为真。 另外记得带着括号吧。
                minprice = p
            elif (p - minprice) > maxprofit:
                maxprofit = p - minprice
        return maxprofit

"""
keep two variable, minprice and maxprofit
"""