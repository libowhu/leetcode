# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x + 1

        while l < r:
            m = l + (r - l) // 2
            if m ** 2 > x:
                r = m
            else:
                l = m + 1

        return l - 1

