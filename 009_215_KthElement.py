"""

"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]




"""
解析github纲领的三种解法：
1. In python, the function that sorts an array is "sorted"
The time is O(NlogN), space is O(1).
因此我们是不是可以理解为sorted函数底层算法用了堆排序，也算是最稳定中最快的排序算法。

2. Java中用 proiorityQueue 就相当于启用 堆排序了（大顶堆或小顶堆），但可以自己控制二叉堆长度
time is O(NlongK) space is O(K)

3. 这种方法基于漫画算法的快速排序（双边循环法），但优化了一些
因为我们只关心Kth element，首先我们不需要递归结构（栈结构），也就进一步省了space complexity，变为O(1)
另外，我们只找partition函数的output: pivot，使其等于K。也就省了一些时间复杂度。但我不懂怎么就变成O(N)了，遍历一次就行了？？ 
答：leetCode解释了平均就是O(N).
FYI, 快速排序本身（Quicksort），time is O(NlogN), space is O(logN)
"""