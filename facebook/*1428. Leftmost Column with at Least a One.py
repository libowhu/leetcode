# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        def binary_search(matrix, target, row_num, col_num):
            left = 0
            right = col_num - 1
            while left < right:
                mid = (left + right) // 2
                if matrix.get(row_num, mid) == target:
                    right = mid
                else:
                    left = mid + 1
            if matrix.get(row_num, left) == target:
                return left
            return -1

        rows, cols = binaryMatrix.dimensions()
        result = cols
        for i in range(rows):
            index = binary_search(binaryMatrix, 1, i, cols)
            if index != -1:
                result = min(result, index)
        if result == cols:
            return -1
        else:
            return result

