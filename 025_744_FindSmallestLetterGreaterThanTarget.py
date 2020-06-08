"""
3 level solution:
1. Record Letters Seen
2. Linear Scan
3. Binary Search (python 二分法 直接用bisect, 上一个题不能用是因为，我们不知道插入谁，要插入的是sqrt，而我们就是要求sqrt的)

  time space
1. N    1
2. N    1
3. logN   1
"""
# solution 1
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        seen = set(letters)
        for i in xrange(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand
"""
这里可以看到字符和ASCII码的转换函数 chr() ord()
不知道为什么第一步为什么要转集合set()
"""

# =======================================
# solution 3
# 正确的解题思路

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        index = bisect.bisect_right(letters,target)
        return letters[index % len(letters)]

"""
据我所知，bisect.bisect() 和 bisect.bisect_right() 没有任何区别。
这里 %len(letters) 很巧妙， 因为如果target插入到letters是最后一个值，那直接可以返回letters第一个值。
"""