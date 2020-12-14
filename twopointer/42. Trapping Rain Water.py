# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: return 0

        l, r = 0, n - 1
        l_max, r_max = height[l], height[r]

        result = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] > l_max:
                    l_max = height[l]
                else:
                    result += l_max - height[l]
                l += 1
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    result += r_max - height[r]
                r -= 1

        return result