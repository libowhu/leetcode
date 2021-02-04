# https://leetcode.com/problems/serialize-and-deserialize-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def pre_order(node):
            if node:
                left = pre_order(node.left)
                right = pre_order(node.right)
                return str(node.val) + "," + left + "," + right
            else:
                return "#"

        return pre_order(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
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
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
