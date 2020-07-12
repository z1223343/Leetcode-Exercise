"""
3 level solutions:
1. Recursion with memoization
2. DP
3. BFS

     time    space
1.  O(n**n)  O(n)
2.  O(n**n)  O(n)
3.  O(n**n)  O(n)
"""

# solution 2:
# 我感觉这个题归为完全背包问题有点牵强。
# 这个是问有没有的问题，不是问有多少或者最少可以多少的问题

# solution 2.1 (from Leetcode)
# 这个我能懂，就是一个普通的DP.
# 而且就是一个一维的DP table, 而且对于worddict的遍历我们用hashset查找解决了。
"""tmd，看起来怎么简单的问题怎么这么复杂啊，脑子不够用啊。
我终于想明白了..关于是dp[j] dp[i]的意思是什么，s[j:i]还是s[j+1:i]还是s[j:i+1]这种index的问题，有点难解释，
因为我也不知道下次再看不明白是哪里不明白，简单说几句吧：
1.所有Index怎么设置，先看dp的需要，因为我们不能整一个dp[-1]
2.这个题i的设置就不是根据s这个string来的，i-1才是s的index
3.因为j注定最大等于i-1，j阴差阳错和s的index对上号了
2.in summary, dp[t]的意义是，s[:t-1]是不是可以在字典里找到。
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordset = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        return dp[len(s)]


# solution 2.2 (from github guideline)
# "求解顺序的完全背包问题时，对物品的迭代应该放在最里层，对背包的迭代放在外层，只有这样才能让物品按一定顺序放入背包中"
# 反正我是不太明白
# 阿sir，我悟了。这个思路本质上和上面的解法是一样的，只不过在第二阶循环上，这里是拿着word去试行不行，上面的解法是拿着index到word里去试行不行。
# 因为这里是拿着word去循环试，也就导致了这个DP还是一个二维的DP，和背包思想是相似的。也因为这个DP是个二维DP，dp[i]还是有传承的关系(dp[i]=dp[i] or ...)
# Note 这里的 i 也是index跟着dp走，所以第一阶循环是range(1,n+1)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            for word in wordDict:
                len_w = len(word)
                if len_w<=i and word==s[i-len_w:i]:
                    dp[i] = dp[i] or dp[i-len_w]
        return dp[n]