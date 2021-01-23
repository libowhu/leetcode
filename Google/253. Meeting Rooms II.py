# https://leetcode.com/problems/meeting-rooms-ii/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        sorted_starts = sorted(starts)
        sorted_ends = sorted(ends)

        res = 0
        cum = 0
        p1, p2, n = 0, 0, len(sorted_starts)
        while p1 < n and p2 < n:
            if sorted_starts[p1] < sorted_ends[p2]:
                cum += 1
                p1 += 1
            elif sorted_starts[p1] > sorted_ends[p2]:
                cum -= 1
                p2 += 1
            else:
                p1 += 1
                p2 += 1
            res = max(res, cum)
        return res

    class Solution:
        def minMeetingRooms(self, intervals: List[List[int]]) -> int:
            if not intervals: return 0
            sorted_intervals = sorted(intervals, key=lambda x: x[0])
            heap = []

            for interval in sorted_intervals:
                start, end = interval
                if heap and heap[0] <= start:
                    heapq.heappop(heap)
                    heapq.heappush(heap, end)
                else:
                    heapq.heappush(heap, end)
            return len(heap)

