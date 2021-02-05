# https://leetcode.com/problems/number-of-closed-islands/
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def printgrid(board):
            for i in range(n):
                temp = []
                for j in range(m):
                    temp.append(board[i][j])
                print(temp)

        def dfs(board, x, y):
            result = True
            if (x == 0 or x == n - 1 or y == 0 or y == m - 1) and board[x][y] == 0:
                return False
            board[x][y] = 2
            for x1, y1 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x2 = x + x1
                y2 = y + y1

                if 0 <= x2 < n and 0 <= y2 < m and board[x2][y2] == 0:
                    result = result and dfs(board, x2, y2)
            return result

        def deep_copy(board):
            new_grid = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    new_grid[i][j] = board[i][j]
            return new_grid

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and 0 < i < n - 1 and 0 < j < m - 1:
                    if dfs(deep_copy(grid), i, j):
                        dfs(grid, i, j)
                        res += 1
        return res
