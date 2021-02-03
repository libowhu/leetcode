# https://leetcode.com/problems/number-of-matching-subsequences/
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        hashmap = collections.defaultdict(list)
        for i, c in enumerate(S):
            hashmap[c].append(i)

        def match(s, word):
            pre = -1
            for c in word:
                cur = bisect.bisect_right(hashmap[c], pre)
                if cur == len(hashmap[c]):
                    return False
                pre = hashmap[c][cur]
            return True

        res = 0
        for word in words:
            if match(S, word):
                res += 1
        return res
