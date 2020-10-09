# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(nums, bound):
            if not nums or nums[-1] > bound: return None
            num = nums.pop()
            root = TreeNode(num)
            root.left = helper(nums, num)
            root.right = helper(nums, bound)
            return root

        return helper(preorder[::-1], sys.maxsize)
    




