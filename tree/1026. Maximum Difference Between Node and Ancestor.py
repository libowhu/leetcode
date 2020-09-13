# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node):
            cur_val = cur_min = cur_max = node.val
            cur_res = 0
            if node.left:
                l_min, l_max, l_res = dfs(node.left)
                cur_min = min(cur_min, l_min)
                cur_max = max(cur_max, l_max)
                cur_res = max(abs(l_min - cur_val), abs(l_max - cur_val), l_res, cur_res)
            if node.right:
                r_min, r_max, r_res = dfs(node.right)
                cur_min = min(cur_min, r_min)
                cur_max = max(cur_max, r_max)
                cur_res = max(abs(r_min - cur_val), abs(r_max - cur_val), r_res, cur_res)
            return cur_min, cur_max, cur_res

        return dfs(root)[2]



