# https://leetcode.com/problems/unique-binary-search-trees/
class Solution:
    def numTrees(self, n: int) -> int:
        self.dp = {0: 1, 1: 1}

        def dfs(n):
            if n in self.dp:
                return self.dp[n]

            count = 0
            for i in range(1, n + 1):
                left = dfs(i - 1)
                right = dfs(n - i)
                count += left * right
            self.dp[n] = count
            return count

        return dfs(n)