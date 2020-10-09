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

        def pre_order(node, output):
            output.append(node.val)
            if node.left:
                pre_order(node.left, output)
            if node.right:
                pre_order(node.right, output)

        output = []
        if root:
            pre_order(root, output)
        return json.dumps(output)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nums = json.loads(data)

        def build(nums, bound):
            if not nums or nums[-1] > bound:
                return None
            num = nums.pop()
            root = TreeNode(num)
            root.left = build(nums, num)
            root.right = build(nums, bound)
            return root

        return build(nums[::-1], sys.maxsize)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans