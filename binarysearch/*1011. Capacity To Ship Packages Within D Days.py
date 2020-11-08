# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)

        def count(weights, cap):
            days = 1
            n = len(weights)
            cur_sum = 0
            for w in weights:
                cur_sum += w
                if cur_sum > cap:
                    cur_sum = w
                    days += 1
            return days

        while l < r:
            m = l + (r - l) // 2
            days = count(weights, m)
            if days <= D:
                r = m
            else:
                l = m + 1
        return l
