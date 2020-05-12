"""
6 level solutions in total:

1: pure brute force: assume a,b are integer in (0,sart(c)), need a 2-level loop.
2: better brute force: since we know 1+3+5+... can be some number's square. Use this to check b. But still 2-level loop.
3: using sqrt function. 1 1-level loop, do sqrt function for every loop.
4: binary Search. Using binary search to check if c-a^2 is a perfect square. not better than level 3.: Fermat theorem. .....
6: two points: it is actually a problem that: In a sorted list find a sum of two elements to satisfy a requirement.

1. Time: O(c). Space: O(1)
2. Time: O(c). Space: O(1)
3. Time: O(sqrt(c)log(c)). Space: O(1)
4. Time: O(sqrt(c)log(c)). Space: O(log(C))
5. Time: O(sqrt(c)log(c)). Space: O(1)
6. Time: O(sqrt(c)). Space: O(1)

"""

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        j = int(sqrt(c))
        while i <= j:
            if i**2 + j**2 == c:
                return True
            elif i**2 + j**2 < c:
                i += 1
            else:
                j -= 1
        return False

"""
0 is integer.

In python, a**2 is square.

In python, int(a) is 向下取整, round(a) is 四舍五入, match.ceil(a) is 向上取整.

In this problem. Note that we can get the potential info that a,b are in (0,sqrt(c)), which is a sorted list.
Also note that a, b can be same number.

"""