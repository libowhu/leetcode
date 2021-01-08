# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window = sum(cardPoints[:k])
        result = window
        for i in range(k-1, -1, -1):
            window += cardPoints[n-k+i]-cardPoints[i]
            result = max(result, window)
        return result
