# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from queue import PriorityQueue
        queue = PriorityQueue()
        for num in nums:
            if queue.qsize() == k:
                queue.put(num)
                queue.get()
            else:
                queue.put(num)
        return queue.get()
