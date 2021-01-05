# https://leetcode.com/problems/alien-dictionary/
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                graph[c] = set()

        for word1, word2 in zip(words[:-1], words[1:]):
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    graph[c2].add(c1)
                    break
            min_len = min(len(word1), len(word2))
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""

        queue = collections.deque([])
        for vertex in graph:
            if len(graph[vertex]) == 0:
                queue.append(vertex)

        output = []
        while queue:
            vertex = queue.popleft()
            output.append(vertex)
            for v in graph:
                if vertex in graph[v]:
                    graph[v].remove(vertex)
                    if len(graph[v]) == 0:
                        queue.append(v)

        for vertex in graph:
            if len(graph[vertex]) != 0:
                return ""

        return "".join(output)