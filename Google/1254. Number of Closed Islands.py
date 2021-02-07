# https://leetcode.com/problems/number-of-closed-islands/
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cache = set()

        def isValid(x, y):
            return 0 <= x < n and 0 <= y < m

        def dfs(board, x, y):
            if isValid(x, y) and board[x][y] == 0 and (x, y) not in cache:
                cache.add((x, y))
                if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                    self.result = False

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(board, x + dx, y + dy)

        self.result = True
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i, j) not in cache:
                    dfs(grid, i, j)
                    if self.result == True:
                        res += 1
                    self.result = True
        return res
