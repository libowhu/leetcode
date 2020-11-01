# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        temp = 0
        result = sys.maxsize

        for i in range(n):
            temp += nums[i]
            if temp < s:
                continue
            else:
                while j <= i and temp >= s:
                    result = min(result, i - j + 1)
                    temp -= nums[j]
                    j += 1

        if result == sys.maxsize:
            return 0
        else:
            return result