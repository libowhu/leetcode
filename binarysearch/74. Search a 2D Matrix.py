# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False

        l, r = 0, m * n

        while l < r:
            mid = l + (r - l) // 2

            row = mid // n
            column = mid % n

            if matrix[row][column] == target:
                return True
            if matrix[row][column] > target:
                r = mid
            else:
                l = mid + 1

        return False
