# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(preorder, start, end):
            if start > end:
                return None
            node = TreeNode(preorder[start])
            index = start + 1
            while index <= end and preorder[index] < preorder[start]:
                index += 1
            node.left = dfs(preorder, start + 1, index - 1)
            node.right = dfs(preorder, index, end)
            return node

        return dfs(preorder, 0, len(preorder) - 1)

