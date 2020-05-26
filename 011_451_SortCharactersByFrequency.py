"""
3 level solutions:
1. array and sorting
2. Hashmap and sorting
3. Bucket Sort (不是计数排序？）

1. time: O(NlogN)   space: O(N)
2. time: O(N+klogK) space: O(N)
3. time: O(N)       space: O(N)

"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        string_builder = []

        for letter, freq in count.most_common():
            string_builder.append(letter * freq)

        return ''.join(string_builder)


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = collections.Counter(s)
        max_freq = max(counts.values())

        buckets = [[] for _ in range(max_freq + 1)]  # magic coding way, two demention list
        for c, j in counts.items():  # counts.items()
            buckets[j].append(c)  # python is so convinient that we don't need to check the each array length for each buckets. Alright java also.

        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):  # Note that we need to traverse from the ending
            for c in buckets[i]:
                string_builder.append(c * i)
        return ''.join(string_builder)

"""
python lambda 匿名函数用法:
https://blog.csdn.net/SeeTheWorld518/article/details/46959593
忘了我是为了哪个题查的这个知识点了、
"""