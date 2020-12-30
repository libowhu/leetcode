# https://leetcode.com/problems/sudoku-solver/
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def deepCopy(src, tar):
            n = len(src)
            for i in range(n):
                for j in range(n):
                    tar[i][j] = src[i][j]

        def getNums(board, x, y):
            used_nums_x = []
            used_nums_y = []
            used_nums_square = []
            for i in range(n):
                if board[i][y] != '.':
                    used_nums_y.append(board[i][y])
            for j in range(n):
                if board[x][j] != '.':
                    used_nums_x.append(board[x][j])

            x1 = (x // 3) * 3
            x2 = ((x // 3) + 1) * 3 - 1
            y1 = (y // 3) * 3
            y2 = ((y // 3) + 1) * 3 - 1

            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if board[i][j] != '.':
                        used_nums_square.append(board[i][j])

            used_nums = set(used_nums_x + used_nums_y + used_nums_square)
            nums = set([str(i) for i in range(1, 10)]) - used_nums
            return nums

        def helper(board, points, result):
            n = len(board)
            if len(points) == 0:
                deepCopy(board, result)
                return

            x, y = points[-1]
            nums = getNums(board, x, y)
            for num in nums:
                board[x][y] = num
                points.pop()
                helper(board, points, result)
                points.append((x, y))
                board[x][y] = '.'

        n = len(board)
        points = [(i, j) for i in range(n) for j in range(n) if board[i][j] == '.']
        result = [['0'] * n for _ in range(n)]
        helper(board, points, result)
        deepCopy(result, board)
