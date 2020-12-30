"""
1. Recursive
2. Using Preorder Traversal (其实就是把tree变为string,在检测是不是sstring包含了tstring)

     time              space
1.   O(MN)              O(N)
2.  O(m^2+n^2+mn)      O(max(m,n))
"""

# solution 1: (速度有点慢)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equals(x,y):
            if x is None and y is None:
                return True
            if x is None or y is None:
                return False
            return x.val==y.val and equals(x.left,y.left) and equals(x.right,y.right)
        if s is None:
            return False
        return equals(s,t) or (self.isSubtree(s.left,t)) or (self.isSubtree(s.right,t))



# solution 2 (leetcode 时间最快答案) （迁客骚人多会于此）但根据时间自由度分析，这个方法理论上没那么快
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def preorder(s):
            return '#' + str(s.val) + preorder(s.left) + preorder(s.right) if s else '%' # note str(s.val) 转换成字符串
        return preorder(t) in preorder(s)




# 错误示范 （我自己写的）
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        if s == t:   # tree 不能拿来直接比较
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)