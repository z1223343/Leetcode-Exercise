"""
3 level solutions:
1. merge and sort: simply use nums1[:] = sorted(nums1[:m] + nums2)   OMG!
2. Two pointers (from the beginning)
3. Two pointers (from the end)

1. Time: O((n+m)log(n+m)) Space: O(1)
2. Time: O(n+m). Space: O(m)
3. Time: O(n+m). Space: O(1)
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = n + m - 1

        while (p1 >= 0) or (p2 >= 0):
            if p1 < 0:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
            elif p2 < 0:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
        return nums1

"""
这个题啊 亲测最后return 有没有都行，Java 和 C++ 比较容易判断需不需要return (看函数是void还是int...)
但python我不知道怎么判断
"""