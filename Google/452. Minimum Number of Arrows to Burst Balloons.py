# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[0])
        pre = None
        res = []

        for point in sorted_points:
            if not res:
                pre = point
                res.append(pre)
            else:
                if res[-1][1] >= point[0]:
                    res[-1] = (max(res[-1][0], point[0]), min(res[-1][1], point[1]))
                else:
                    res.append(point)
        return len(res)
