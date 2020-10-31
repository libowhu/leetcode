# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        def binary_search(array, target):
            l, r = 0, len(array)
            while l < r:
                m = l + (r - l) // 2
                if array[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        array = []
        for num in nums:
            if not array:
                array.append(num)
                continue
            index = binary_search(array, num)
            if index == len(array):
                array.append(num)
            else:
                array[index] = num

        return len(array)
