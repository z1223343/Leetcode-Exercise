"""
5 level solutions:
1. brute force. It takes me half a day to understand
2. DP (using starting points)
3. DP (using ending points)
4. Greedy Algorithm (starting points)
5. Greedy Algorithm (ending points)

1. time O(2**n) space O(n)
2. time O(n**2) space O(n)
3. time O(n**2) space O(n)
4. time O(nlogn) space O(1)
5. time O(nlogn) space O(1)
"""

"""
About Greedy Algorithm:

The idea of greedy algorithm is to pick the locally optimal move at each step, that will lead to the globally optimal solution.
"""

# Greedy Approach (sort starting points)
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[0])
        result = 0       # 这个result是舍弃的数量，即需要删除的数量
        prev = None
        for curr in intervals:
            if prev and prev[1]>curr[0]:
                result += 1
                if prev[1]>curr[1]:
                    prev = curr
            else:
                prev = curr
        return result


# Greedy Approach (sort ending points)
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        result = 0
        prev = None
        for curr in intervals:
            if (not prev) or prev[1] <= curr[0]:
                result += 1       # result means 保留
                prev = curr
        return len(intervals) - result



"""
此题leetCode解答撰写者是个棒槌。不要细看。理解思路就好。


"""