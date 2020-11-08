# https://leetcode.com/problems/koko-eating-bananas/
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, sum(piles)

        def helper(piles, m):
            output = 0
            for pile in piles:
                if pile % m == 0:
                    output += pile // m
                else:
                    output += pile // m + 1
            return output

        while l < r:
            m = l + (r - l) // 2
            if helper(piles, m) <= H:
                r = m
            else:
                l = m + 1
        return l
