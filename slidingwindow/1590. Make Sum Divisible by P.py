# https://leetcode.com/problems/make-sum-divisible-by-p/
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        result = n = len(nums)
        prefix = 0
        hashmap = {0: -1}
        k = sum(nums) % p
        if k == 0: return 0

        for r in range(n):
            prefix = (prefix + nums[r]) % p
            if (prefix - k) % p in hashmap:
                result = min(result, r - hashmap[(prefix - k) % p])
            hashmap[prefix] = r

        return -1 if result == n else result
