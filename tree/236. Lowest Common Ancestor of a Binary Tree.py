# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node, p, q):
            if node == None: return None
            if node.val == p.val or node.val == q.val: return node
            left_return = lca(node.left, p, q)
            right_return = lca(node.right, p, q)
            if left_return is None: return right_return
            if right_return is None: return left_return
            return node
        return lca(root, p, q)