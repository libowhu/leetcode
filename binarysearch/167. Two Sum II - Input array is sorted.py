# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            elif s == target:
                return [l + 1, r + 1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            target_num1 = numbers[i]
            target_num2 = target - target_num1
            if target_num2 < 0:
                continue

            left, right = i + 1, n
            while left < right:
                mid = left + (right - left) // 2
                if numbers[mid] == target_num2:
                    return [i + 1, mid + 1]
                if numbers[mid] > target_num2:
                    right = mid
                else:
                    left = mid + 1

            return [-1, -1]



