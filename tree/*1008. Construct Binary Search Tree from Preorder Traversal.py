# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def find(target, start, end):
            output = start
            while output < end:
                if preorder[output] > target:
                    break
                output += 1
            return output

        def helper(start, end):
            if start == end: return None
            mid = find(preorder[start], start + 1, end)
            root = TreeNode(preorder[start])
            root.left = helper(start + 1, mid)
            root.right = helper(mid, end)
            return root

        return helper(0, len(preorder))




