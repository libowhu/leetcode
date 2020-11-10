# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

        def helper(dp, size):
            for i in range(size, n + 1):
                for j in range(size, m + 1):
                    sum = dp[i][j] - dp[i][j - size] - dp[i - size][j] + dp[i - size][j - size]
                    if 0 < sum <= threshold:
                        return True
            return False

        l, r = 1, min(m, n) + 1
        while l < r:
            mid = l + (r - l) // 2
            if helper(dp, mid):
                l = mid + 1
            else:
                r = mid

        return l - 1

