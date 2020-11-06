# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        l_val, r_val = nums[l], nums[r - 1]

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > r_val:
                l = m + 1
            else:
                r = m

        return nums[l]