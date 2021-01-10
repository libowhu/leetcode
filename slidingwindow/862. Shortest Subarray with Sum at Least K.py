# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        B = [0] * (n + 1)
        for i in range(1, n + 1):
            B[i] = B[i - 1] + A[i - 1]

        min_deque = collections.deque()

        res = sys.maxsize
        for r in range(n + 1):
            num = B[r]
            while min_deque and num < B[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(r)
            while num - B[min_deque[0]] >= K:
                res = min(res, r - min_deque[0])
                min_deque.popleft()

        return res if res != sys.maxsize else -1
