# https://leetcode.com/problems/non-overlapping-intervals/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1: return 0
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        res = 0
        pre = sorted_intervals[0]
        for i in range(1, len(intervals)):
            start, end = sorted_intervals[i]
            if pre[1] > start:
                res += 1
                pre[1] = min(pre[1], end)
            else:
                pre = sorted_intervals[i]
        return res
