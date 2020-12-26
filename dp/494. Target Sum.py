# https://leetcode.com/problems/target-sum/
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        if (sum(nums) + S) % 2 != 0:
            return 0
        target = (sum(nums) - S) // 2
        if target < 0: return 0

        dp = [[0] * (target + 1) for _ in range(n + 1)]

        dp[0][0] = 1
        for i in range(1, n + 1):
            if nums[i - 1] == 0:
                dp[i][0] = 2 * dp[i - 1][0]
            else:
                dp[i][0] = dp[i - 1][0]

        for j in range(1, target + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][target]
