# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()

        def backtracking(nums, temp, visited, result):
            if len(temp) > len(nums): return
            if len(temp) == len(nums):
                result.append(temp.copy())

            for num in nums:
                if num in visited:
                    continue
                temp.append(num)
                visited.add(num)
                backtracking(nums, temp, visited, result)
                temp.pop()
                visited.remove(num)

        backtracking(nums, [], visited, result)
        return result
