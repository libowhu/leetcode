# https://leetcode.com/problems/interval-list-intersections/
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(A)
        m = len(B)

        def is_overlap(interval_a, interval_b):
            return max(interval_a[0], interval_b[0]) <= min(interval_a[1], interval_b[1])

        def merge(interval_a, interval_b):
            return [max(interval_a[0], interval_b[0]), min(interval_a[1], interval_b[1])]

        i, j = 0, 0
        while i < n and j < m:
            interval_a = A[i]
            interval_b = B[j]

            if is_overlap(interval_a, interval_b):
                res.append(merge(interval_a, interval_b))

            if interval_a[1] > interval_b[1]:
                j += 1
            else:
                i += 1
        return res
