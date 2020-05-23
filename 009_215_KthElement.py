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

# 和LeetCode答案略不同，我的patition用双边循环，尽量按我思路来吧，别人的代码都看着别扭

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(startindex, endindex):
            pivot = random.randint(startindex, endindex)
            nums[pivot], nums[startindex] = nums[startindex], nums[pivot]
            pivotvalue = nums[startindex]

            left = startindex
            right = endindex

            while left < right: # 不能有等于，不然是死循环，超出时间限制
                while nums[right] > pivotvalue and left < right:  # 一个很骚的地方就在这个针对right的循环必须在下一个针对left的循环，不然永远是错的。因为我们想让left和right最后重合在<=pivot的部分。不然就把>pivot的元素换到最左面了。
                    right -= 1
                while nums[left] <= pivotvalue and left < right:
                    left += 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]

            nums[startindex], nums[left] = nums[left], nums[startindex]
            return left

        k = len(nums) - k
        startindex = 0
        endindex = len(nums) - 1
        while startindex < endindex:
            tmp = partition(startindex, endindex)
            if tmp == k:
                break
            elif tmp < k:
                startindex = tmp + 1
            else:
                endindex = tmp - 1
        return nums[k] # 注意缩进，return 在 while 外面


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
答：leetCode解释了平均就是O(N). woc 我悟了，time complexity = 1+1/2+1/4+1/8+...~=2, so it is O(N)
FYI, 快速排序本身（Quicksort），time is O(NlogN), space is O(logN)
"""

"""
In python, 交换一个array里两个序号的值，不需要像java一样加一个中间变量，一共三个值互换，直接：
nums[a],nums[b] = nums[b],nums[a] 有点吊 
"""