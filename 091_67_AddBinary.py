"""
1 level solution:
1. math

time: O(max(M,N))   space：O(max(M,N))
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a),len(b))
        carry = 0
        a = a.zfill(n)
        b = b.zfill(n)
        res = []
        for i in range(n-1,-1,-1):
            if a[i] == "1":
                carry+=1
            if b[i] == "1":
                carry+=1
            if carry%2 == 1:
                res.append(1)
            else:
                res.append(0)
            carry//=2
        if carry==1:
            res.append(1)
        res.reverse()
        return "".join(map(str,res))


# .zfill() str 右对齐 前面补0的method. 这也有... library是第一生产力...