# https://leetcode.com/problems/subarray-product-less-than-k/
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = count = 0
        cur_prod = 1

        for r in range(n):
            cur_prod *= nums[r]
            while r >= l and cur_prod >= k:
                cur_prod /= nums[l]
                l += 1
            count += r - l + 1
        return count
