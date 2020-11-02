# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bi_search_lower_bound(nums, target):
            index = -1
            l, r = 0, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    index = m
                    r = m
                elif nums[m] > target:
                    r = m
                else:
                    l = m + 1
            return index

        def bi_search_upper_bound(nums, target):
            index = -1
            l, r = 0, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    index = m
                    l = m + 1
                elif nums[m] > target:
                    r = m
                else:
                    l = m + 1
            return index

        index_left = bi_search_lower_bound(nums, target)
        index_right = bi_search_upper_bound(nums, target)

        return [index_left, index_right]