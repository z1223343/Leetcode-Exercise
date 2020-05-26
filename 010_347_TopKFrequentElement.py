"""
2 level solutions:
1. Heap: hashmap -> a heap of size k -> output array
2. Quickselect.

1. time: O(Nlogk) space: O(N+k)
2. time: O(N) (worst O(N**2))  space: O(N)
"""
"""keep both 2 level solution answer, all are good and useful"""

from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # consider seperately to make sure the time complexity smaller than NlogN.
        if k == len(nums):
            return nums

        # build hash map: character and how often it appears
        count = Counter(nums)

        # build heap of to k frequent elements
        # and convert it into an output array
        res = heapq.nlargest(k, count.keys(), key=count.get)
        return res

"""
about 'res = heapq.nlargest(k, count.keys(), key=count.get)":

heapq.nlargest can do smallest heap + output array at one step.
counter function can output the results as sub-class of dict, so it also has the methods of dict class, including'get'

heapq.nlargest(n, iterable[, key]), key is an optional augument, which should be a FUNCTION that is used to 
extract a comparison key from each element in the iterable. key=str.lower Equivalent to: sorted(iterable, key=key, reverse=True)[:n]

if we only do: heapq.nlargest(n, iterable.keys()) or heapq.nlargest(n, iterable.values()) should give the only top k smallest .keys() or .values(), instead of top k of keys() based on values().

"""

# use Quickselect algorithm, then too similar with Q215
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        unique = list(count.keys())

        def partition(startindex, endindex):
            pivot = random.randint(startindex, endindex)
            unique[pivot], unique[startindex] = unique[startindex], unique[pivot]
            pivotvalue = count[unique[startindex]]       # notice what we essentially compare is count.value not the key

            left = startindex
            right = endindex

            while left < right:
                while left < right and count[unique[right]] > pivotvalue: # notice
                    right -= 1
                while left < right and count[unique[left]] <= pivotvalue: # notice
                    left += 1
                if left < right:
                    unique[left], unique[right] = unique[right], unique[left]

            unique[startindex], unique[left] = unique[left], unique[startindex]
            return left

        n = len(unique)
        k = n - k
        startindex = 0
        endindex = n - 1
        while startindex < endindex:
            tmp = partition(startindex, endindex)
            if tmp == k:
                break
            elif tmp > k:
                endindex = tmp - 1
            else:
                startindex = tmp + 1
        return unique[k:]
