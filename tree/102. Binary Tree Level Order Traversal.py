# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        if root is None: return output

        queue = collections.deque([root])
        while queue:
            temp = []
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(temp)
        return output