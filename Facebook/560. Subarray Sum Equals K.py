# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        record = collections.defaultdict(int)
        record[0] = 1
        count = 0
        acc = 0

        for i in range(n):
            acc += nums[i]
            if acc - k in record:
                count += record[acc - k]
            record[acc] += 1

        return count

