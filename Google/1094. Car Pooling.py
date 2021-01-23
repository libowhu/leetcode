# https://leetcode.com/problems/car-pooling/
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        starts = sorted([(trip[1], trip[0]) for trip in trips], key=lambda x: x[0])
        ends = sorted([(trip[2], trip[0]) for trip in trips], key=lambda x: x[0])

        p1, p2, n = 0, 0, len(trips)
        count = 0
        while p1 < n and p2 < n:
            if starts[p1][0] == ends[p2][0]:
                count += starts[p1][1] - ends[p2][1]
                p1 += 1
                p2 += 1
            elif starts[p1][0] > ends[p2][0]:
                count -= ends[p2][1]
                p2 += 1
            else:
                count += starts[p1][1]
                p1 += 1
            if count > capacity:
                return False
        return True
