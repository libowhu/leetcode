# https://leetcode.com/problems/word-break-ii/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        hashmap = {}
        cache = {}
        for word in wordDict:
            hashmap[word] = 1

        def helper(s):
            if s in cache: return cache[s]
            result = []
            if s in hashmap:
                result.append([s])

            for i in range(1, len(s)):
                word = s[:i]
                remain = s[i:]
                if word in hashmap:
                    left_words = [[word]]
                    right_words = helper(remain)
                    result.extend([x + y for x in left_words for y in right_words])
            cache[s] = result
            return result

        output = helper(s)
        result = []
        for item in output:
            result.append(" ".join(item))
        return result
