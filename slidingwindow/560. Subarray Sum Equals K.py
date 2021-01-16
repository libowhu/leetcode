# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hashmap = {0: 1}
        count = cur_sum = 0

        for r in range(n):
            cur_sum += nums[r]
            if cur_sum - k in hashmap:
                count += hashmap[cur_sum - k]
            if cur_sum in hashmap:
                hashmap[cur_sum] += 1
            else:
                hashmap[cur_sum] = 1
        return count
