"""


"""
# solution 1: 我这是严格按照 backtracking 的思路来写的，体现了backtrack.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return
        res = []
        init_list = [str(root.val)]
        def backtrack(curr_node,curr_list):
            if (not curr_node.left and not curr_node.right):
                res.append('->'.join(curr_list))
            if curr_node.left:
                curr_list.append(str(curr_node.left.val))
                backtrack(curr_node.left,curr_list)
                curr_list.pop()
            if curr_node.right:
                curr_list.append(str(curr_node.right.val))
                backtrack(curr_node.right,curr_list)
                curr_list.pop()
        backtrack(root,init_list)
        return res


# 我的反面教材：需要注意的是，这样是不行的，虽然看上去我用了next_list，好像loop里的每个backtrack都有了自己崭新的curr_list和next_list，
# 实际上还是会相互影响的，比如说题目里的example，会得到["1->2->5","1->2->5->3"]

# 应该是和matlab不太一样,matlab里就算重复的变量名在每个子function里也是崭新的。
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root.val:
            return
        res = []
        init_list = [str(root.val)]
        def backtrack(curr_node,curr_list):
            if (not curr_node.left and not curr_node.right):
                res.append('->'.join(curr_list))
            if curr_node.left:
                next_list = curr_list
                next_list.append(str(curr_node.left.val))
                backtrack(curr_node.left,next_list)
            if curr_node.right:
                next_list = curr_list
                next_list.append(str(curr_node.right.val))
                backtrack(curr_node.right,next_list)
        backtrack(root,init_list)
        return res

# ======================================================================
# solution 2：（leetcode solution)
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths
                else:
                    path += '->'  # extend the current path
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths
"""
这里我好好分析一下：
1. 这里recursive算法并没有体现出backtrack，而只是一个递归遍历，因为它用了‘path' which is a string instead of list. 在这种情况下
    它是可以不回溯的，其实这也是我一开始的想法（上面的错误案例），但是我当初用了list作为变量，每个递归的函数的重复变量是相互影响的，
    而string不会，这里可能是python对于指针的设定的一个差别，我记得说当string改变时其实是创造了一个新的string，而list不是。结案了。
    这个知识点之前一个题目 我也有所发现好像。
2. 所以这里我做了一个实验，用现在这个recursive solution的code，把path改为list而不是string，果然这个算法就不好用了：
"""
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path.append(str(root.val))
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths
                else:
                    path.append('->')  # extend the current path
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, [])
        return paths
"""
output: [["1","->","2","->","5","3"],["1","->","2","->","5","3"]]
他这个更惨，由于没有像我一样, 用next_list进行左右树的区分，所以两个答案是一样的。
"""