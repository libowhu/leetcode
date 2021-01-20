# https://leetcode.com/problems/meeting-rooms/
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        pre_interval = sorted_intervals[0]
        for interval in sorted_intervals[1:]:
            if max(pre_interval[0], interval[0]) < min(pre_interval[1], interval[1]):
                return False
            pre_interval = interval
        return True
