# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        queue = collections.deque([])

        def in_order(root, queue):
            if root is None:
                queue.append(None)
            else:
                queue.append(root.val)
                in_order(root.left, queue)
                in_order(root.right, queue)

        in_order(root, queue)
        return queue

    def deserialize(self, data):
        def helper(data):
            val = data.popleft()
            if val is None:
                return None
            else:
                node = TreeNode(val)
                node.left = helper(data)
                node.right = helper(data)
                return node

        root = helper(data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))