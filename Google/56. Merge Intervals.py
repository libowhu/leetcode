# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if len(res) == 0:
                res.append(interval)
                continue
            if res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(interval[1], res[-1][1])
        return res


