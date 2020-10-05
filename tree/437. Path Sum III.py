# https://leetcode.com/problems/path-sum-iii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        self.count = 0

        def dfs(node, sum, targets):
            next_targets = []
            for target in targets:
                if target - node.val == 0:
                    self.count += 1
                next_targets.append(target - node.val)
            next_targets.append(sum)
            if node.left:
                dfs(node.left, sum, next_targets)
            if node.right:
                dfs(node.right, sum, next_targets)

        if root is None:
            return self.count
        dfs(root, sum, [sum])
        return self.count
