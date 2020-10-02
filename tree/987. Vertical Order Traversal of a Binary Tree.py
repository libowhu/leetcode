# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, x, y, elements):
            if node is not None:
                val = node.val
                if x in elements:
                    elements[x].append((y, val))
                else:
                    elements[x] = [(y, val)]
                dfs(node.left, x - 1, y + 1, elements)
                dfs(node.right, x + 1, y + 1, elements)

        elements = {}
        dfs(root, 0, 0, elements)

        output = []
        sorted_keys = sorted(elements.keys())
        for key in sorted_keys:
            sorted_elements = sorted(elements[key], key=lambda x: (x[0], x[1]))
            output.append([x[1] for x in sorted_elements])
        return output

