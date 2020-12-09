# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cache = set()
        result = []
        n = len(nums)

        def helper(temp, index, n):
            if index == n:
                t_temp = tuple(temp)
                if t_temp not in cache:
                    cache.add(t_temp)
                    result.append(t_temp)
                return

            helper(temp, index + 1, n)
            helper(temp + [nums[index]], index + 1, n)

        helper([], 0, n)
        return result