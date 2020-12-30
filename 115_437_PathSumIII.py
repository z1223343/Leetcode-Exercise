"""
1. Recursive Prefix Sum

     time   space
1.   O(N)    O(N)
"""

# solution 1:
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count = 0
        k = sum
        h = defaultdict(int)

        def prefix_sum(root ,sum_curr):

            nonlocal count  # note 这个句法

            if root is None:
                return count

            sum_curr += root.val

            if sum_curr == k:
                count += 1

            count += h[sum_curr - k]

            h[sum_curr] += 1

            count = prefix_sum(root.left, sum_curr)
            count = prefix_sum(root.right, sum_curr)

            h[sum_curr] -= 1

            return count

        return prefix_sum(root ,0)


# solution 1 (leetcode 答案子函数不带返回值的写法)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node:
                return

                # current prefix sum
            curr_sum += node.val

            # here is the sum we're looking for
            if curr_sum == k:
                count += 1

            # number of times the curr_sum − k has occurred already,
            # determines the number of times a path with sum k
            # has occurred up to the current node
            count += h[curr_sum - k]

            # add the current sum into hashmap
            # to use it during the child nodes processing
            h[curr_sum] += 1

            # process left subtree
            preorder(node.left, curr_sum)
            # process right subtree
            preorder(node.right, curr_sum)

            # remove the current sum from the hashmap
            # in order not to use it during
            # the parallel subtree processing
            h[curr_sum] -= 1

        count, k = 0, sum
        h = defaultdict(int)
        preorder(root, 0)
        return count