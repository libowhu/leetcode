#https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        hashmap = collections.defaultdict(int)
        for idx, c in enumerate(S):
            hashmap[c] = idx

        result = []
        left = right = 0
        for idx, c in enumerate(S):
            right = max(right, hashmap[c])
            if idx == right:
                result.append(right - left + 1)
                left = right = right + 1
        return result