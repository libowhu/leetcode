# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = -sys.maxsize

        def dfs(root):
            if root is None:
                return 0
            else:
                left_max = dfs(root.left)
                right_max = dfs(root.right)
                value = root.val

                self.max_sum = max(self.max_sum, value, value + left_max, value + right_max,
                                   value + left_max + right_max)
                return max(value, value + left_max, value + right_max)

        dfs(root)
        return self.max_sum