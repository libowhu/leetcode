# https://leetcode.com/problems/4sum-ii/
import itertools


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = map(sum, itertools.product(A, B))
        CD = map(sum, itertools.product(C, D))

        hashmap = collections.defaultdict(int)
        for e in CD:
            hashmap[e] += 1

        result = 0
        for e in AB:
            if -e in hashmap:
                result += hashmap[-e]

        return result
