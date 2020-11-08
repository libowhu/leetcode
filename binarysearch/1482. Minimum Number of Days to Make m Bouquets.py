# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = 1, max(bloomDay) + 1

        def count(bloomDay, k, d):
            output = 0
            cur_sum = 0
            for i in bloomDay:
                if i <= d:
                    cur_sum += 1
                else:
                    output += cur_sum // k
                    cur_sum = 0
            output += cur_sum // k
            return output

        while l < r:
            mid = l + (r - l) // 2
            if count(bloomDay, k, mid) >= m:
                r = mid
            else:
                l = mid + 1
        return l if l < max(bloomDay) + 1 else -1
