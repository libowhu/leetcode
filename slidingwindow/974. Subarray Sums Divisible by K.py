# https://leetcode.com/problems/subarray-sums-divisible-by-k/
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)
        hashmap = {0: 1}
        count = prefix = 0

        for i in range(n):
            prefix = (prefix + A[i]) % K
            if prefix in hashmap:
                count += hashmap[prefix]
                hashmap[prefix] += 1
            else:
                hashmap[prefix] = 1

        return count
