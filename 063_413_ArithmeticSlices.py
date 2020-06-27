"""
4 level solutino (brute force 略)
1. using recursion
2. DP
3. DP with constant space
4. using formula

    time   space
1.  O(n)    O(n)
1.  O(n)    O(n)
1.  O(n)    O(1)
1.  O(n)    O(1)
"""

# solution 2
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = 0
        total = 0
        for i in range(2,len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp += 1
                total += dp
            else:
                dp = 0
        return total


# solution 3
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = 0
        total = 0
        for i in range(2,len(A)):  # 从2开始
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp += 1
                total += dp
            else:
                dp = 0
        return total

# solution 4 (玩数学的，也没什么意思)
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count = 0
        total = 0
        for i in range(2,len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                count+=1
            else:
                total+=count*(count+1)//2  # 注意要返回int 所以用//
                count = 0
        total+=count*(count+1)//2  # 注意循环完 还要加一次
        return total