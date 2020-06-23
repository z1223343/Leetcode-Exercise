"""
1 solution:
1. Backtracking

time: 评论区百家争鸣,我觉得就是O(N*N!)吧
space: O(N!)
"""
# solution 1 （leetcode solution):
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            if first == n - 1:
                res.append(nums[:])  # Note!如何这里写append(nums)，那就错了，最后各个组合都一样，因为nums是传引用（指针）
            else:
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first + 1)
                    nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


# 反面案例，curr_list是个list,传的是指针，这样写代码 结果都乱了。
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(curr_list, suffix):
            if not suffix:
                _ = curr_list
                res.append(_)
            for index, i in enumerate(suffix):
                curr_list.append(i)
                suffix.pop(index)
                backtrack(curr_list, suffix)
                curr_list.pop()
                suffix.append(i)
        backtrack([], nums)
        return res
# 针对反面案例的改正： （这么写submit是成功的，但就是有点绕，空间也没有很优化）
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(curr_list, suffix):
            if not suffix:
                res.append(curr_list[:])
            for index, i in enumerate(suffix[:]):
                curr_list.append(i)
                tmp = suffix[:]
                suffix.pop(index)
                backtrack(curr_list, suffix[:]) # 这里亲测传curr_list[:]也不影响结果
                curr_list.pop()
                suffix = tmp
        backtrack([], nums)
        return res
"""
关于python函数传参：
https://blog.csdn.net/liuxiao214/article/details/81673093

当我们传的参数是int、字符串(string)、float、（数值型number）、元组（tuple) 时，无论函数中对其做什么操作，
都不会改变函数外这个参数的值；
当传的是字典型(dictionary)、列表型(list)时，如果是重新对其进行赋值，则不会改变函数外参数的值，如果是对其进行操作，则会改变。

关于nums和nums[:]的区别：
https://blog.csdn.net/u010558281/article/details/53355211
"""