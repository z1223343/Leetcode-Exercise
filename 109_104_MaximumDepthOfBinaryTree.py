"""
1. recursion
2. iteration

"""

# solution 1: (DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left,right)+1


# solution 2:
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []: # note "stack is not None" 就错了。 [] is not None.
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth

"""
这个方法要注意的是，如果stack.append((a,b)),可以直接 x,y = stack.pop()
"""