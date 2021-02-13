# https://leetcode.com/problems/divisor-game/
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N+1)
        for i in range(1, N+1):
            for j in range(1, i):
                if i % j == 0 and not dp[i-j]:
                    dp[i] = True
                    break
        return dp[N]
