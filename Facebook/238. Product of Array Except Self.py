# https://leetcode.com/problems/product-of-array-except-self/
# Solution 1: two accumulated arrays, O(n), O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        acc1 = [1] * n
        acc2 = [1] * n
        result = [1] * n

        for idx in range(1, n):
            acc1[idx] = acc1[idx - 1] * nums[idx - 1]
            acc2[n - idx - 1] = acc2[n - idx] * nums[n - idx]

        for idx in range(n):
            result[idx] = acc1[idx] * acc2[idx]

        return result

# Solution 2: replace accumulated array with accumulated variable, O(n), O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [1] * n

        left = 1
        right = 1
        for idx in range(1, n):
            left = left * nums[idx - 1]
            right = right * nums[n - idx]

            result[idx] = result[idx] * left
            result[n - idx - 1] = result[n - idx - 1] * right

        return result

