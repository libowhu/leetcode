# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(amount):
            if amount in dp: return dp[amount]
            if amount == 0: return 0
            temp = []
            for coin in coins:
                if amount - coin >= 0:
                    temp.append(dfs(amount-coin))
                else:
                    temp.append(float('inf'))
            dp[amount] = min(temp) + 1
            return dp[amount]
        res = dfs(amount)
        return res if res != float('inf') else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1