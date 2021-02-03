# https://leetcode.com/problems/find-duplicate-subtrees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        duplicate = {}
        res = []

        def preorder(node):
            if node:
                left = preorder(node.left)
                right = preorder(node.right)
                cur_s = str(node.val) + "l" + left + "r" + right
                if cur_s in duplicate:
                    n, c = duplicate[cur_s]
                    if c == 1:
                        res.append(n)
                    duplicate[cur_s] = (n, c + 1)
                else:
                    duplicate[cur_s] = (node, 1)
                return cur_s
            else:
                return ""

        preorder(root)
        return res
