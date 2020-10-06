# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        start_of_level = root
        while start_of_level:
            cur_level_cur_node = start_of_level
            next_level_pre_node = None
            while cur_level_cur_node:
                next_level_nodes = [cur_level_cur_node.left, cur_level_cur_node.right]
                for node in next_level_nodes:
                    if node:
                        if not next_level_pre_node:
                            next_level_pre_node = node
                        else:
                            next_level_pre_node.next = node
                            next_level_pre_node = node
                cur_level_cur_node = cur_level_cur_node.next
            start_of_level = start_of_level.left
        return root
