# https://leetcode.com/problems/longest-mountain-in-array/
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3: return 0

        up = down = result = 0
        for i in range(1, n):
            if down and arr[i - 1] < arr[i] or arr[i - 1] == arr[i]:
                up = down = 0
            if arr[i - 1] < arr[i]: up += 1
            if arr[i - 1] > arr[i]: down += 1
            if down and up:
                result = max(result, up + down + 1)
        return result

