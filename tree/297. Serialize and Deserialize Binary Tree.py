# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        nums = []

        def pre_order(root, nums):
            if root is None:
                nums.append(None)
            else:
                nums.append(root.val)
                pre_order(root.left, nums)
                pre_order(root.right, nums)

        pre_order(root, nums)
        return json.dumps(nums)

    def deserialize(self, data):
        nums = json.loads(data)

        def helper(data):
            val = data.pop()
            if val is None:
                return None
            else:
                node = TreeNode(val)
                node.left = helper(data)
                node.right = helper(data)
                return node

        root = helper(nums[::-1])
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))