# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0

        def inorder(node, heap):
            if node:
                left = inorder(node.left, heap)
                self.count += 1
                heapq.heappush(heap, (-self.count, node.val))
                if len(heap) > k:
                    heapq.heappop(heap)
                right = inorder(node.right, heap)

        heap = []
        inorder(root, heap)
        return heap[0][1]