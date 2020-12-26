# https://leetcode.com/problems/last-stone-weight-ii/
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        s = sum(stones)
        dp = [[False] * (s + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for j in range(1, s + 1):
            dp[0][j] = False

        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if j >= stones[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        for m in range(s // 2, -1, -1):
            if dp[n][m] == True:
                return s - 2 * m
        return 0
