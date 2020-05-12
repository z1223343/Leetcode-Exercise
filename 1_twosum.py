"""
3 level solutinos:
1. brute force: 1 level-1 loop; 1 Level-2 loop.
2. Two-pass hash table: 2 level-1 loop. give all data to dict, then find target-num.
3. One-pass hash table: 1 level-1 loop. fill dict and find target-num at the same time.

1. [Time O(n^2). Space O(1)]
2. [Time O(n). Space O(n)]
3. [Time O(n). Space O(n)]
"""

class solution(object):
    def twosum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            re = target - num
            if re not in h:
                h[num] = i
            else:
                return [h[re],i]


"""
For dict,
to search if the dict has a certain key

can use:
1. if key in dict
2. if key in dict.keys()
3. if dict.has_key(key)

https://blog.csdn.net/tao546377318/article/details/52160942

"""