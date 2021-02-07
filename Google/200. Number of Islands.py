# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def isValid(grid, x, y):
            return 0 <= x < n and 0 <= y < m

        def dfs(grid, x, y):
            if isValid(grid, x, y) and grid[x][y] == '1' and (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(grid, x + dx, y + dy)

        res = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == '1':
                    dfs(grid, i, j)
                    res += 1
        return res
