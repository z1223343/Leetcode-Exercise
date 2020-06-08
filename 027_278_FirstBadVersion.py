"""
2 level solution
1. brute force (stupid)
2. binary search (this problem is a very standard binary search problem)

   time   space
1.  N      1
2. logN    1
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l<h:
            mid = l+(h-l)//2   # note l+(h-l)//2， I wrote it wrong at first
            if isBadVersion(mid):
                h = mid
            else:
                l = mid+1   # Here we garantee this is not a deatch loop, cuz l will always be the one when there are only 2 elements, and we have +1 to let l==h. (我好想说的不太对这里,但这里确实保证了收敛)
        return l