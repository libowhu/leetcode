# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        output = []
        reverse = False
        while queue:
            level_length = len(queue)
            vals = []
            for _ in range(level_length):
                node = queue.popleft()
                vals.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if reverse:
                vals = vals[::-1]
            reverse = not reverse
            output.append(vals)
        return output

