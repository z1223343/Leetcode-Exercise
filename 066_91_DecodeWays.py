"""
3 level solution:

2.

"""

# solution 2 (DP思想是真丫的牛逼)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0]!='0' else 0
        for i in range(2,len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            two_digit = int(s[i-2:i])
            if two_digit<27 and two_digit>=10:  # 注意啊这里<10不行，容易漏了
                dp[i] += dp[i-2]
        return dp[-1]
# 牛逼，脑子快想烂了。

# 耀中改：这样更 straight-foward点，s[0]=='0'不用试别的了。 循环前面这么改：
        if s[0] == '0':
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1

# 耀中再改: 如果你非要dp[i] 管0~i原数组的组合方式（原解法是0~i-1） 也可以的，则code应改为:
# 为了把这个dp[1]提前算出来，要好多个if啊，不如答案那种简洁
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * len(s)
        dp[0] = 1
        two_digit = int(s[0:2])
        if two_digit <= 26:
            if s[1] == '0':
                dp[1] = 1
            else:
                dp[1] = 2
        else:
            if s[1] == '0':
                dp[1] = 0
            else:
                dp[1] = 1

        for i in range(2, len(s)):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            two_digit = int(s[i - 1:i + 1])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]

# 其实我发现，如果有一位dp[i] == 0，则答案肯定==0。而且此时一定是有0。


"""
对于DP思想，自我总结，有以下流水线：
1.先想如何大问题化小问题，也就是这个题目的dp公式是什么，(这个题是 dp[i] = dp[i-1]+d[i-2] (根据情况有些是 dp[i]=dp[i-1])，
2.有了公式后，想dp数列应该如何初始化，长度是多少，初始值为0还是inf
3.代一代最初的几个值，看一开始的dp[0] dp[1] dp[2]等应该做怎样的调整，能正确的循环起来吗。
4.能不能优化space complexity，也就是我们为了求dp[i],是不是只需要某几个特定的值 比如dp[i-1] dp[i-2]。
"""