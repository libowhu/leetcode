# https://leetcode.com/problems/missing-element-in-sorted-array/
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def count(nums, index):
            return nums[index] - nums[0] - index

        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if count(nums, m) >= k:
                r = m
            else:
                l = m + 1
        return nums[l - 1] + k - count(nums, l - 1)
