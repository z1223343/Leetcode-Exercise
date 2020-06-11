"""
4 level solutions
1. brute force
2. DP
3. Greedy
4. BFS
5. Mathematics

4. time O(N**(h/2))   space O(N**(h/2))
"""
# 只看BFS怎么解
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

        queue = (n,)
        level = 0

        while queue:
            level += 1
            next_queue = set()  # use set to reduce time dramatically

            for i in queue:
                for square in square_nums:
                    if square == i:
                        return level
                    elif square < i:
                        next_queue.add(i - square)  # set添加是add,不是append
            queue = next_queue

"""
每个问题都有自己的特殊性，解题时用相应的大类算法中进行微调，
像这个题，因为我们遇到相同的中间结果，只需要保留一个，
所以queue没有用队列结构，用的set，下一个level用新set直接替换掉旧的set.
"""

# 这个题可以回来继续深挖