# https://leetcode.com/problems/evaluate-division/
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(set)
        for equation, value in zip(equations, values):
            start, end = equation
            graph[start].add((end, value))
            graph[end].add((start, 1.0 / value))

        def dfs(graph, start, end, temp, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return temp
            for cur, value in graph[start]:
                if cur not in visited:
                    visited.add(cur)
                    output = dfs(graph, cur, end, temp * value, visited)
                    visited.remove(cur)
                    if output != -1.0:
                        return output
            return -1.0

        output = []
        for query in queries:
            start, end = query
            visited = {start}
            val = dfs(graph, start, end, 1.0, visited)
            output.append(val)
        return output
