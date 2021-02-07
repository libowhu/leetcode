# https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def isValid(grid, x, y):
            return 0 <= x < n and 0 <= y < m

        def dfs(grid, x, y):
            if isValid(grid, x, y) and grid[x][y] == 1 and (x, y) not in visited:
                visited.add((x, y))
                res = 1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    res += dfs(grid, x + dx, y + dy)
                return res
            return 0

        res = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == 1:
                    res = max(res, dfs(grid, i, j))
        return res
