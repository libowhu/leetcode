# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        A = [0] * (n + 1)

        for i in range(n):
            A[i + 1] = A[i] + nums[i]

        def binary_search(A, target):
            l, r = 0, len(A)
            while l < r:
                m = l + (r - l) // 2
                if A[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        result = sys.maxsize
        for i in range(n):
            index = binary_search(A, s + A[i])
            if index != len(A):
                result = min(result, index - i)

        return 0 if result == sys.maxsize else result