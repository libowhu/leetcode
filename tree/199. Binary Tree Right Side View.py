# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None: return []

        queue = collections.deque([(root, 1)])
        elements = {1: root}

        while queue:
            node, level = queue.popleft()
            elements[level] = node
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        sorted_keys = sorted(elements.keys())
        output = []
        for key in sorted_keys:
            val = elements[key].val
            output.append(val)

        return output
