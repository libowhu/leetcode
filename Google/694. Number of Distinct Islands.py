# https://leetcode.com/problems/number-of-distinct-islands/
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def isValid(grid, x, y):
            return 0 <= x < n and 0 <= y < m

        def dfs(grid, x, y):
            rx = sys.maxsize
            ry = sys.maxsize
            points = []
            if isValid(grid, x, y) and (x, y) not in visited and grid[x][y] == 1:
                visited.add((x, y))
                rx = min(rx, x)
                ry = min(ry, y)
                points.append((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    tx, ty, tpoints = dfs(grid, x + dx, y + dy)
                    rx = min(rx, tx)
                    ry = min(ry, ty)
                    points = points + tpoints
            return rx, ry, points

        res = set()
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == 1:
                    mx, my, points = dfs(grid, i, j)
                    if points:
                        shape = tuple([(x - mx, y - my) for x, y in points])
                        if shape not in res:
                            res.add(shape)
        return len(res)
