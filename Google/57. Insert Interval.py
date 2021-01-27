# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # nlogn
        newIntervals = sorted(intervals + [newInterval], key=lambda x:x[0])
        res = [newIntervals[0]]
        for interval in newIntervals[1:]:
            if res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

        # n
        res = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval
            elif interval[1] >= newInterval[0] or interval[0] >= newInterval[1]:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        res.append(newInterval)
        return res

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            cur_start, cur_end = interval
            if cur_start > newInterval[1]:
                res.append(newInterval)
                newInterval = interval
            elif cur_end < newInterval[0]:
                res.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        res.append(newInterval)
        return res
