# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        hashmap = {}
        for idx, num in enumerate(inorder):
            hashmap[num] = idx

        def dfs(preorder, inorder, pre_start, in_start, in_end):
            if in_start > in_end:
                return None
            root_val = preorder[pre_start]
            root_node = TreeNode(root_val)

            index = hashmap[root_val]
            root_node.left = dfs(preorder, inorder, pre_start + 1, in_start, index - 1)
            root_node.right = dfs(preorder, inorder, pre_start + index - in_start + 1, index + 1, in_end)

            return root_node

        return dfs(preorder, inorder, 0, 0, len(inorder) - 1)
