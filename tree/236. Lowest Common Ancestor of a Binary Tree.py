# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = (-1, None)

        def dfs(node, level, p_val, q_val):
            if node is None:
                return 0

            left = dfs(node.left, level + 1, p_val, q_val)
            right = dfs(node.right, level + 1, p_val, q_val)
            current = 1 if node.val in (p_val, q_val) else 0

            count = left + right + current

            if count >= 2:
                if level > self.result[0]:
                    self.result = (level, node)
            return 1 if count > 0 else 0

        dfs(root, 0, p.val, q.val)
        return self.result[1]
