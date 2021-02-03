# https://leetcode.com/problems/delete-nodes-and-return-forest/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)

        def dfs(node, parent, direction):
            if not node: return
            if node.val in to_delete:
                if node.left and node.left.val not in to_delete:
                    res.append(node.left)
                if node.right and node.right.val not in to_delete:
                    res.append(node.right)

                if parent and direction == 1:
                    parent.left = None
                if parent and direction == 2:
                    parent.right = None
            dfs(node.left, node, 1)
            dfs(node.right, node, 2)

        if not root: return []
        if root.val not in to_delete:
            res.append(root)
        dfs(root, None, 0)
        return res
