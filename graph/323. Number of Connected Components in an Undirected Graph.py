# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: set() for i in range(n)}
        visited = set()

        for edge in edges:
            a, b = edge
            graph[a].add(b)
            graph[b].add(a)

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        result = 0
        for i in range(n):
            if i not in visited:
                result += 1
                dfs(i)

        return result