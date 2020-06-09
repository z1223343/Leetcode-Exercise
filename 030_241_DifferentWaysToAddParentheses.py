"""
1 solution
1. Divide and Conquer (LeetCode 无解答)
"""
# 为啥我的算法时间faster than 5.91%， 还有啥好算法？
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ans=[]

        for i,char in enumerate(input):
            if char=='+' or char=='-' or char=='*':
                lefts = self.diffWaysToCompute(input[:i])
                rights = self.diffWaysToCompute(input[i+1:])
                for left in lefts:
                    for right in rights:
                        if char=='+':
                            ans.append(left+right)
                        elif char=='-':
                            ans.append(left-right)
                        else:
                            ans.append(left*right)
        if not ans:
                return [int(input)]
        return ans