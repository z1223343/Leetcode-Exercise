"""
1. BFS

     time   space
1.   O(N)    O(M) (max number of node in one level)
"""


# solution 1: 讲道理，我这个答案比原版还好点
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        que = collections.deque()
        res = []

        que.append(root)
        while que:aaaaa
            tmp = 0
            size = len(que)  # len()
            for i in range(size):  # for i in range(1) 只执行一次 i=0
                node = que.popleft()  # 这句要在前
                tmp += node.val
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            res.append(tmp / size)
        return res
# 参考：https://blog.csdn.net/fuxuemingzhu/article/details/79088554