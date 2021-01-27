# https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        hashmap = collections.defaultdict()
        for idx, c in enumerate(S):
            hashmap[c] = idx
        output = []
        left, right = 0, 0
        for idx, c in enumerate(S):
            right = max(right, hashmap[c])
            if idx == right:
                output.append(right - left + 1)
                left = right + 1
        if left <= right:
            output.append(right - left + 1)
        return output
