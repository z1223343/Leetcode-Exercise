"""
2 level solutions:
1.DP
2.Greedy

    time      space
1.  O(n**2)   O(n)
2.  O(n*logn)  O(n)
"""

# solution 1:
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort() # 与上一题相比，这里多了个sort，因为这个题选取各元素的顺序是可以任意的，sort之后保证了前面的元素肯定不会连接到后面的元素，进而我们顺序loop就遍历了所有的情况。好好想想这个逻辑吧弟弟。
        dp = [1] * len(pairs)
        for i in range(0,len(pairs)):
            for j in range(0,i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

# solution 2:
# 我真的惊了，这什么神仙算法，这么简单的逻辑，竟然就好使
# time score: 2000+ms -> less than 200ms
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        curr, ans = float('-inf'), 0
        pairs = sorted(pairs, key=operator.itemgetter(1)) # Note operator.itemgetter(n) returns a function
        for x,y in pairs:
            if curr < x:
                curr = y
                ans += 1
        return ans

"""
about operator.itemgetter 函数理解：
https://blog.csdn.net/qq_22022063/article/details/79019294
"""