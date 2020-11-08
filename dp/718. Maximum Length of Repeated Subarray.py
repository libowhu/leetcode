# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            if A[i] == B[0]:
                dp[i][0] = 1

        for i in range(m):
            if A[0] == B[i]:
                dp[0][i] = 1

        result = 0
        for i in range(1, n):
            for j in range(1, m):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])

        return result
