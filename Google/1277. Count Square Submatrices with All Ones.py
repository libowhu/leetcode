# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            dp[i][0] = matrix[i][0]

        for i in range(m):
            dp[0][i] = matrix[0][i]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0
        res = 0
        for i in range(n):
            for j in range(m):
                res += dp[i][j]
        return res
