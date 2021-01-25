# https://leetcode.com/problems/add-bold-tag-in-string/
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        intervals = []
        n = len(s)
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if s[i:j] in dict:
                    intervals.append([i, j])

        if len(intervals) < 1: return s
        res = ""
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if output[-1][1] >= intervals[i][0]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])

        res, pre_end = "", 0
        for idx, interval in enumerate(output):
            start, end = interval
            res += s[pre_end:start] + "<b>" + s[start:end] + "</b>"
            pre_end = end
        res += s[pre_end:]
        return res

