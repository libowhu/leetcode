# https://leetcode.com/problems/shortest-distance-to-a-character/
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        result = [0 if c == C else n for c in S]
        for i in range(1, n):
            result[i] = min(result[i], result[i - 1] + 1)
        for j in range(n - 2, -1, -1):
            result[j] = min(result[j], result[j + 1] + 1)
        return result
