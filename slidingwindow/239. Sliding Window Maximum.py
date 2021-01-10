# https://leetcode.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_deque = collections.deque()
        res = []
        for r in range(n):
            if r < k - 1:
                while max_deque and nums[r] > nums[max_deque[-1]]:
                    max_deque.pop()
                max_deque.append(r)
            else:
                while max_deque and nums[r] > nums[max_deque[-1]]:
                    max_deque.pop()
                max_deque.append(r)

                l = r - k + 1

                if l > max_deque[0]:
                    max_deque.popleft()
                res.append(nums[max_deque[0]])
        return res
