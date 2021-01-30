# https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(word, index, board, i, j, visited):
            if board[i][j] != word[index]:
                return False

            index += 1
            if index == len(word):
                return True

            n = len(board)
            m = len(board[0])

            result = False
            points = [(i + delta[0], j + delta[1]) for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
            for point in points:
                a, b = point
                if 0 <= a < n and 0 <= b < m and (a, b) not in visited:
                    visited.add((a, b))
                    result = result or search(word, index, board, a, b, visited)
                    visited.remove((a, b))
            return result

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                visited = set()
                visited.add((i, j))
                if search(word, 0, board, i, j, visited):
                    return True
        return False
