# https://leetcode.com/problems/longest-mountain-in-array/
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3: return 0

        up = [0] * n
        down = [0] * n
        mountain = [0] * n

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up[i] = up[i - 1] + 1

        for j in range(n - 2, -1, -1):
            if arr[j] > arr[j + 1]:
                down[j] = down[j + 1] + 1

        for k in range(1, n - 1):
            if up[k] and down[k]:
                mountain[k] = up[k] + down[k]

        return 0 if max(mountain) == 0 else max(mountain) + 1
