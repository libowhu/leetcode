# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, r = matrix[0][0], matrix[n - 1][n - 1]

        def helper(matrix, target):
            n = len(matrix)
            row, col = 0, n - 1
            number = 0

            while row <= n - 1 and col >= 0:
                if matrix[row][col] <= target:
                    number += col + 1
                    row += 1
                else:
                    col -= 1
            return number

        while l < r:
            m = l + (r - l) // 2
            count = helper(matrix, m)
            if count >= k:
                r = m
            else:
                l = m + 1

        return l
