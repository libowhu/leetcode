# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque, min_deque = collections.deque(), collections.deque()
        n = len(nums)
        l = 0
        res = 1

        for r in range(n):
            num = nums[r]
            while max_deque and num > nums[max_deque[-1]]:
                max_deque.pop()
            while min_deque and num < nums[min_deque[-1]]:
                min_deque.pop()
            max_deque.append(r)
            min_deque.append(r)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                if l > max_deque[0]:
                    max_deque.popleft()
                if l > min_deque[0]:
                    min_deque.popleft()

            res = max(res, r - l + 1)
        return res
