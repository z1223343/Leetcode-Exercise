"""
1. top-down recursion
2. bottom-up recursion

     time   space
1.   O(N)    O(NlogN)
2.   O(N)    O(N)
"""

# solution 1:
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            ans = abs(self.height(root.left)-self.height(root.right))<2
            return ans and self.isBalanced(root.left) and self.isBalanced(root.right) # 但是这个样子啊，好像会造成多余的计算，最理想的情况是有一个sub tree判为不平衡就可以直接给出最终答案了。
    def height(self,root: TreeNode) -> int:
        if root is None:
            return -1
        else:
            return 1+max(self.height(root.left),self.height(root.right))




# solution 2:
