# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = [0] * (n + 1)
        for i in range(1, n + 1):
            A[i] = A[i - 1] + nums[i - 1]

        hashmap = {}
        result = 0
        for r in range(n + 1):
            if A[r] - k in hashmap:
                result = max(result, r - hashmap[A[r] - k])
            if A[r] not in hashmap:
                hashmap[A[r]] = r
        return result
