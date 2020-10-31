# https://leetcode.com/problems/random-pick-with-weight/
class Solution:

    def __init__(self, w: List[int]):
        self.weights = [0] * (len(w) + 1)
        sum = 0
        for idx, e in enumerate(w):
            sum += e
            self.weights[idx + 1] = sum

    def pickIndex(self) -> int:
        random = randint(1, self.weights[-1])
        l, r = 1, len(self.weights)
        while l < r:
            m = l + (r - l) // 2
            if self.weights[m] >= random:
                r = m
            else:
                l = m + 1
        return l - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()