class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        ma, mi = max(A), min(A)
        if ma - K <= mi + K:
            return 0
        else:
            return ma - mi - 2 * K
