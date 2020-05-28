"""
1 solution:
贪心思想
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        gi = si = 0
        while gi<len(g) and si<len(s):
            if g[gi] > s[si]:
                si += 1
            else:
                gi += 1
                si += 1
        return gi

# 分清哪个变量是饼干，哪个变量是孩子。 最后的result是数孩子，每次循环里都要自增的是饼干。

# Same:
        while gi<len(g) and si<len(s):
            if g[gi] <= s[si]:
                gi+=1
            si+=1
        return gi