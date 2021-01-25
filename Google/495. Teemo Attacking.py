# https://leetcode.com/problems/teemo-attacking/
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        intervals = [[t, t + duration] for t in timeSeries]
        if len(intervals) < 1: return 0
        start, end, res = intervals[0][0], intervals[0][1], 0
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                end = intervals[i][1]
            else:
                res += end - start
                start = intervals[i][0]
                end = intervals[i][1]
        res += end - start
        return res
