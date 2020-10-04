# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        adjacency_list = {}

        def build_tree(node, parent, adjacency_list):
            connections = []
            if parent:
                connections.append(parent)
            if node.left:
                build_tree(node.left, node, adjacency_list)
                connections.append(node.left)
            if node.right:
                build_tree(node.right, node, adjacency_list)
                connections.append(node.right)
            adjacency_list[node.val] = connections

        def bfs(start, K, adjacency_list):
            queue = collections.deque([(start, 0)])
            visited = {start.val}
            result = []
            while queue:
                node, level = queue.popleft()
                if level == K:
                    result.append(node.val)
                if level > K:
                    return result
                nodes = adjacency_list[node.val]
                for connection in connections:
                    if connection.val not in visited:
                        visited.add(connection.val)
                        queue.append((connection, level + 1))
            return result

        build_tree(root, None, adjacency_list)
        return bfs(target, K, adjacency_list)
