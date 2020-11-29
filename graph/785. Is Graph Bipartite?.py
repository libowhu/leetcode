# https://leetcode.com/problems/is-graph-bipartite/
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {i: 0 for i in range(n)}
        neighbors = {i: set() for i in range(n)}

        for index, nodes in enumerate(graph):
            neighbors[index] = set(nodes)

        def dfs(node_index, color_index):
            result = True
            if color[node_index] == 0:
                color[node_index] = color_index
                nodes = neighbors[node_index]
                for node in nodes:
                    if color[node] == color_index:
                        return False
                    elif color[node] == 0:
                        result = result and dfs(node, -1 * color_index)
            return result

        for i in range(n):
            if not dfs(i, 1):
                return False
        return True
