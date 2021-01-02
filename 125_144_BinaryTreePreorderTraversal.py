"""
1. DFS (preorder)
2. Morris Traversal (要不考虑output size，space complexity is O(1))

     time   space
1.   O(N)    O(H)
2.   O(N)    O(H)
"""

# solution 1:
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return res

# solution 2: (挖槽自己写出来的，和答案简直每一行都一样，我牛逼)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        res = []
        while node:
            if node.left is None:
                res.append(node.val)
                node = node.right

            else:
                predecessor = node.left
                while (predecessor.right is not None) and (predecessor.right is not node):
                    predecessor = predecessor.right
                if predecessor.right is None:
                    res.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right
        return res


"""
DFS 总结：
DFS 分为 前序遍历preorder 后序遍历postorder  中序遍历inorder

    1
   / \
  2   3
 / \   \
4   5   6
层次遍历顺序：[1 2 3 4 5 6]
前序遍历顺序：[1 2 4 5 3 6]
中序遍历顺序：[4 2 5 1 3 6]
后序遍历顺序：[4 5 2 6 3 1]

通用解法为Recursive, Interative, Morris_Traversal

Recursive:
前序遍历: do with curr_node
        dfs(node.left)
        dfs(node.right)
中序遍历: dfs(node.left)
        do with curr_node
        dfs(node.right)
后序遍历: dfs(node.left)
        dfs(node.right)
        do with curr_node

Interative:
前序遍历: while stack:
            root = stack.pop()
            do with root
            if root.left:
                stack.append(root.right)
            if root.right:
                stack.append(root.left)
中序遍历: while stack:
            root = stack.pop()
            do with root
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        res = res[::-1]
后序遍历: while stack:
            while root.left:
                stack.append(root.left)
                curr = curr.left
            curr = stack.pop()
            do with root
            curr = curr.right

Morris_Traversal: time:O(n)  space:O(1)  其实我感觉Morris的时间会比前两种方法慢一倍的，因为每个每个node实际上要遍历两次，所以实际time complexity是O(2n)
Preorder:

while node:
    if node.left is None:
        do with node
        node = node.right
    else:
        predecessor = node.left
        while (predecessor.right is not None) and (predecessor.right is not node):
            predecessor = predecessor.right
        if predecessor.right is None:
            do with node            # note
            predecessor.right = node
            node = node.left
        else:
            predecessor.right = None
            node = node.right

Inorder: (想了半天相通了为啥和preorder比，do with node换个位置就行了,因为inorder我们要保证的是在tree的左下角，我们先执行的是第一个大if(node.left is None)
            在执行大else里的小else里的do with code，左右的树干node都要在自己第二次遍历时再append到res。）

while node:
    if node.left is None:
        do with node
        node = node.right
    else:
        pre = node.left
        while (pre.right is not None) and (pre.right is not node):
            pre = pre.right
        if pre.right is None:
            pre.right = node
            node = node.left
        else:
            do with node        # note
            pre.right = None
            node = node.right




BFS 需要结合队列存储结构，即que = collections.deque()  deque.append(node)   node=deque.popleft()
"""