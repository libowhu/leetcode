# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        cur_interval = sorted_intervals[0]
        output = []
        for interval in sorted_intervals[1:]:
            if max(cur_interval[0], interval[0]) <= min(cur_interval[1], interval[1]):
                cur_interval = [min(cur_interval[0], interval[0]), max(cur_interval[1], interval[1])]
            else:
                output.append(cur_interval)
                cur_interval = interval
        output.append(cur_interval)
        return output
