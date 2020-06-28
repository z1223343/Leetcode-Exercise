"""
2 level solutions:
1. DP
2. Math （这个人是玩数学的

"""

# solution 1: （实际上这个方法是不简单的，和数学法比起来
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i],max(j*(i-j),j*dp[i-j])) # 牛逼
        return dp[n]
"""
我尼玛想了半天终于基本上想明白了，
这个DP建立在我们assume，对于一个数的最大乘积，等于比这个数小的一个最大乘积 乘以他们的差，ok我们来找这个数是什么 (就是找i-j)
j代表他们的差，所以j in range(1,i)，对于每个j，比较的对象是 dp[i-j]*j，
但是注意对于比较小的(i-j)值如1,2,3,4，因为他们的dp值比自身小，你不如不拆了，直接乘他们自己。
所以用 max(j*(i-j),j*dp[i-j])。
最后呢和上一个(i-j)比较算出的dp[i]大小，我们要的是最大的。所以: max(dp[i],以上) 
(当然我们知道，j一般都等于3)，不过这个算法还要循环range(1,i)，所以这个算法应该很慢，但是最后time score还不低，可能n测试值都很小。
"""

# solution 1: (这也可以？这不还是数学法吗  dp[i]=dp[i-3]*3
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 0, 1, 2, 4, 6, 9]
        for i in range(7, n + 1):
            dp.append(dp[i - 3] * 3)
        return dp[n]


# solution 2: （自己研究出的方案，time score还行，但是有点绕，你面是现场能反应出来吗，要用纸写写
class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2: return 1
        if n==3: return 2
        a = n//3
        b = n%3
        if b%2 == 0:
            return int(3**a*2**(b/2))
        if b%2 == 1:
            return int(3**(a-1)*4)

# solution 2：（别人的思路总是这么清爽）
class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2: return 1
        if n==3: return 2
        res = 1
        while n>4:
            res*=3
            n-=3
        return res*n
# reference: https://blog.csdn.net/fuxuemingzhu/article/details/80486238



