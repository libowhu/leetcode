# https://leetcode.com/problems/last-stone-weight/
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        c_stones = [-a for a in stones]
        heapq.heapify(c_stones)
        while len(c_stones) > 1:
            h1 = heapq.heappop(c_stones)
            h2 = heapq.heappop(c_stones)
            if h1 == h2:
                continue
            else:
                heapq.heappush(c_stones, h1 - h2)

        if len(c_stones) == 0:
            return 0
        else:
            return -heapq.heappop(c_stones)