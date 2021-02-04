# https://leetcode.com/problems/construct-string-from-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def helper(node):
            if node:
                left = helper(node.left)
                right = helper(node.right)
                if left == "" and right != "":
                    return "(" + str(node.val) + "()" + right + ")"
                return "(" + str(node.val) + left + right + ")"
            else:
                return ""

        return helper(t)[1:-1]
