"""
1 level solution:
1. Divide and Conquer (Recursion)

time: nGn = 4**n/n**(0.5)
space: nGn = 4**n/n**(0.5)
"""


# 看完答案后自己写出来的：

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate_trees(start, end):
            if start > end:
                return [None, ]  # must not be None, because 'None' cannot be iterable.

            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        current_tree = TreeNode(i, left_tree, right_tree)
                        all_trees.append(current_tree)  # 好好看，好好学，弟弟。
            return all_trees

        return generate_trees(1, n) if n else []  # if n else [] 不然return [[]] when n==0

"""
这个代码自己设定的“树”的定义，最后代码输入的答案 例如：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
感觉挺神奇的，python这是自己判断出了这是一个二叉树结构 并且在输出的时候转换成了数组？
"""


""" 
题外话： Github small green box can be made up by modifying local time!
"""