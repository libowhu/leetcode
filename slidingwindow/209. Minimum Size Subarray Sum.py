# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        res = sys.maxsize
        window = 0
        for r in range(n):
            num = nums[r]
            window += num
            while window >= s:
                res = min(res, r-l+1)
                window -= nums[l]
                l += 1
        return 0 if res == sys.maxsize else res
