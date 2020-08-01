"""
1 level solution:
1. math
"""

# solution 1: (我自己写的）
class Solution:
    def convertToTitle(self, n: int) -> str:
        if n==0:
            return ""
        res = ""

        while n>0:
            n-=1
            last = n%26
            res = chr(last+ord("A"))+res
            n = n//26
        return res

# solution 1 (github guideline) 和我其实一样的：
class Solution:
    def convertToTitle(self, n: int) -> str:
        if n==0:
            return ""
        n-=1
        res = self.convertToTitle(n//26)+chr(n%26+ord("A"))
        return res