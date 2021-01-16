# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        if target == 0:
            return n

        l = cur_sum = max_length = 0

        for r in range(n):
            cur_sum += nums[r]
            while r > l and cur_sum > target:
                cur_sum -= nums[l]
                l += 1
            if cur_sum == target:
                max_length = max(max_length, r - l + 1)

        return -1 if max_length == 0 else n - max_length
