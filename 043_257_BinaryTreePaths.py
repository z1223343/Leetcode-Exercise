"""


"""

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








# 反面教材：需要注意的是，这样是不行的，虽然看上去我用了next_list，好像loop里的每个backtrack都有了自己崭新的curr_list和next_list，
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