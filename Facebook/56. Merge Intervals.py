class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for interval in intervals:
            if not output:
                output.append(interval)
            else:
                start, end = output[-1]
                if interval[0] <= end:
                    pre_start, pre_end = output.pop()
                    cur_start = min(pre_start, interval[0])
                    cur_end = max(pre_end, interval[1])
                    output.append([cur_start, cur_end])
                else:
                    output.append(interval)
        return output

