# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n

        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target: return m
            if nums[m] >= nums[0]:
                if nums[m] > target >= nums[0]:
                    r = m
                else:
                    l = m + 1
            if nums[m] <= nums[n - 1]:
                if nums[n - 1] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m
        return -1