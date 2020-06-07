"""
1 solution
1. Greedy         不是典型的greedy，但是很新颖，useful.

time: O(N)  space: O(N)
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {char: index for index, char in enumerate(S)} # dict创建
        archor = 0
        ans = []
        j = 0

        for index, char in enumerate(S):
            j = max(j, last[char])
            if j == index:
                ans.append(j + 1 - archor)
                archor = j + 1
        return ans