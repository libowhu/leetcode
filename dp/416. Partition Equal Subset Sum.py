# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False

        n = len(nums)
        target = sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for j in range(1, target + 1):
            dp[0][j] = False

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]
