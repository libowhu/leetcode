# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(graph, start, temp, output):
            if start == len(graph) - 1:
                output.append(temp.copy())
                return

            for v in graph[start]:
                temp.append(v)
                dfs(graph, v, temp, output)
                temp.pop()

        output = []
        dfs(graph, 0, [0], output)
        return output