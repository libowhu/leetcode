# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if node is None:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            node.left = None
            node.right = None

            if left:
                node.right = left
                copy_node = node
                while copy_node.right is not None:
                    copy_node = copy_node.right
                copy_node.right = right
            else:
                node.right = right
            return node

        dfs(root)
