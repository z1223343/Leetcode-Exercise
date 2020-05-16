"""
2 level solutions:
1. brute force. stupid but needs skills (dynamic programming?). ideas is to get all the sub-strings. will not explain.
2. Two pointers. to check if one string is a sub-string of another string.

1. Time: O(2**n)   Space: O(2**n)
2. Time: O(nx)     Space: O(x)      (n: number of str in d, x: average string length)
"""


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        def isSubstr(sub, target):
            i = 0
            j = 0
            while j < len(target) and i < len(sub):    # lack "i<len(sub)" will cause an error
                if sub[i] == target[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(sub):
                return True
            else:
                return False

        longestword = ''
        for string in d:
            l1 = len(longestword)
            l2 = len(string)
            if l1 < l2 or (l1 == l2 and string < longestword):
                if isSubstr(string, s):
                    longestword = string

        return longestword


"""
in python, comparing two string will refer to lexicographical order.
stringa < stringb,  min(stringa.stringb)
"""