

# solution 1 （leetcode无solution,自己写的，time击败96%)
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        que = collections.deque()
        final_row = []
        que.append(root)
        while que:
            row = []
            size = len(que)
            for i in range(size):
                node = que.popleft()
                row.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return row[0]