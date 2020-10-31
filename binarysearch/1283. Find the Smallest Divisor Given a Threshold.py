# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = l + (r - l) // 2
            if sum(-num//m for num in nums) >= -threshold:
                r = m
            else:
                l = m + 1
        return l