"""
1 level solution:
1. math
time:  O(max(M,N))    space: O(max(M,N))
"""

# solution 1:
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        n = max(len(num1), len(num2))
        num1 = num1.zfill(n)
        num2 = num2.zfill(n)

        for i in range(n - 1, -1, -1):
            x1 = ord(num1[i]) - ord('0')
            x2 = ord(num2[i]) - ord('0')
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
        if carry == 1:
            res.append(1)
        res.reverse()
        return "".join(map(str, res))