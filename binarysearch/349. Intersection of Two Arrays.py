# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))

        n = len(nums1)
        m = len(nums2)

        def binary_search(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    r = m
                else:
                    l = m + 1
            return -1

        result = []
        if n > m:
            for num in nums2:
                index = binary_search(nums1, num)
                if index != -1:
                    result.append(num)
        else:
            for num in nums1:
                index = binary_search(nums2, num)
                if index != -1:
                    result.append(num)

        return result
