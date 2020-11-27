# https://leetcode.com/problems/possible-bipartition/
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        color = {i: 0 for i in range(1, N + 1)}

        for dislike in dislikes:
            a, b = dislike
            graph[a].add(b)
            graph[b].add(a)

        starts = []
        for i in range(1, N + 1):
            if len(graph[i]) != 0:
                starts.append(i)

        def dfs(node, cur_color):
            color[node] = cur_color
            neighbors = graph[node]
            result = True
            for neighbor in neighbors:
                neighbor_color = color[neighbor]
                if neighbor_color == cur_color:
                    result = False
                elif neighbor_color == 0:
                    result = result and dfs(neighbor, -1 * cur_color)
            return result

        for start in starts:
            if color[start] == 0:
                if not dfs(start, 1):
                    return False
        return True
