# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def pre_order(node):
            if node:
                left = pre_order(node.left)
                right = pre_order(node.right)
                return str(node.val) + ',' + left + ',' + right
            else:
                return '#'

        return pre_order(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = collections.deque(data.split(","))

        def decode(queue):
            if queue:
                val = queue.popleft()
                if val == '#':
                    return None
                root = TreeNode(val)
                root.left = decode(queue)
                root.right = decode(queue)
                return root

        return decode(queue)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))