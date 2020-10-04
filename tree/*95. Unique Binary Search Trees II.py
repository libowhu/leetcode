# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        if n == 1: return [TreeNode(1)]

        array = [i for i in range(1, n + 1)]

        def build_bst(array, start, end):
            if start > end:
                return [None]

            output = []
            for index in range(start, end + 1):
                left_nodes = build_bst(array, start, index - 1)
                right_nodes = build_bst(array, index + 1, end)

                for node1 in left_nodes:
                    for node2 in right_nodes:
                        root = TreeNode(array[index])
                        root.left = node1
                        root.right = node2
                        output.append(root)
            return output

        return build_bst(array, 0, n - 1)