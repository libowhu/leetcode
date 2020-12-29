# https://leetcode.com/problems/beautiful-arrangement/
class Solution:
    def countArrangement(self, N: int) -> int:
        def helper(N, nums, temp, result, cache):
            if len(temp) == N:
                result.append(temp.copy())
                return
            pos = len(temp) + 1
            for idx, num in enumerate(nums):
                if num not in cache and (num % pos == 0 or pos % num == 0):
                    temp.append(num)
                    cache.add(num)
                    helper(N, nums, temp, result, cache)
                    temp.pop()
                    cache.remove(num)

        result = []
        cache = set()
        nums = [i + 1 for i in range(N)]
        helper(N, nums, [], result, cache)
        return len(result)