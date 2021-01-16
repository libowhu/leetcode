# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = [0] * (n + 1)
        for i in range(1, n + 1):
            A[i] = A[i - 1] + nums[i - 1]

        count = 0
        hashmap = {}
        for i in range(n + 1):
            if A[i] - k in hashmap:
                count += hashmap[A[i] - k]
            if A[i] in hashmap:
                hashmap[A[i]] += 1
            else:
                hashmap[A[i]] = 1
        return count
