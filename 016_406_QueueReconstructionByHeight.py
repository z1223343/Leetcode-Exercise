"""
1 solution:
Greedy Algorithm

Time O(N**2)  Space O(N)
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x:(-x[0],x[1]))
        output = []
        for p in people:
            output.insert(p[1],p)
        return output

"""
矮个子对于高个子相当于看不见的，
因此先排高个子，再排矮个子。
第二个值k，刚好就应该是插入的位置。
"""