# https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            count = 0
            for i in range(n):
                if nums[i] <= m:
                    count += 1
            if count > m:
                r = m
            else:
                l = m + 1
        return l
