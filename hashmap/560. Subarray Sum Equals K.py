# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        accs = [0] * (n + 1)

        for i in range(n):
            accs[i + 1] = accs[i] + nums[i]

        hashmap = {0: 1}
        result = 0
        for i in range(n):
            if accs[i + 1] - k in hashmap:
                result += hashmap[accs[i + 1] - k]
            if accs[i + 1] not in hashmap:
                hashmap[accs[i + 1]] = 1
            else:
                hashmap[accs[i + 1]] += 1
        return result
