# https://leetcode.com/problems/possible-bipartition/
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        color = {i: 0 for i in range(1, N + 1)}

        for dislike in dislikes:
            a, b = dislike
            graph[a].add(b)
            graph[b].add(a)

        def dfs(node, cur_color):
            result = True
            if color[node] == 0:
                color[node] = cur_color
                for neighbor in graph[node]:
                    neighbor_color = color[neighbor]
                    if neighbor_color == cur_color:
                        return False
                    elif neighbor_color == 0:
                        result = result and dfs(neighbor, -1 * cur_color)
            return result

        for i in range(1, N + 1):
            if not dfs(i, 1):
                return False

        return True