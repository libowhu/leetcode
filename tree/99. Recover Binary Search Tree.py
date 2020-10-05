# https://leetcode.com/problems/recover-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.hashmap = {}

        def in_order(node, result):
            if node:
                in_order(node.left, result)
                result.append(node.val)
                self.hashmap[node.val] = node
                in_order(node.right, result)

        array = []
        in_order(root, array)

        first_pair = None
        second_pair = None
        for pre, cur in zip(array[:-1], array[1:]):
            if pre > cur:
                if not first_pair:
                    first_pair = (pre, cur)
                    continue
                if not second_pair:
                    second_pair = (pre, cur)

        if not first_pair:
            return
        if not second_pair:
            first_node = self.hashmap[first_pair[0]]
            second_node = self.hashmap[first_pair[1]]
        else:
            first_node = self.hashmap[first_pair[0]]
            second_node = self.hashmap[second_pair[1]]
        first_node.val, second_node.val = second_node.val, first_node.val