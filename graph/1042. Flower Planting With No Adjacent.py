# https://leetcode.com/problems/flower-planting-with-no-adjacent/
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = {i: set() for i in range(n)}
        result = [0 for _ in range(n)]
        total_color = {1, 2, 3, 4}

        for path in paths:
            a, b = path
            graph[a - 1].add(b - 1)
            graph[b - 1].add(a - 1)

        for i in range(n):
            result[i] = (total_color - {result[j] for j in graph[i]}).pop()
        return result