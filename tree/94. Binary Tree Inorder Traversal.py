# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        def dfs(node, output):
            if node.left:
                dfs(node.left, output)
            output.append(node.val)
            if node.right:
                dfs(node.right, output)

        if root:
            dfs(root, output)
            return output
        else:
            return []
