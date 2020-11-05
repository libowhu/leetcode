# https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0:
            return False

        row, col = 0, len(matrix[0]) - 1
        while row <= len(matrix) - 1 and col >= 0:
            if matrix[row][col] == target: return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False
