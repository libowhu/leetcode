# https://leetcode.com/problems/k-closest-points-to-origin/
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        from queue import PriorityQueue
        from random import random

        queue = PriorityQueue()
        for point in points:
            queue.put((point[0] ** 2 + point[1] ** 2, random(), point))

        output = []
        for _ in range(K):
            output.append(queue.get()[2])

        return output