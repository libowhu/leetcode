# https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashmap = {}
        cache = {}
        for word in wordDict:
            hashmap[word] = 1

        def helper(s):
            if s in cache:  return cache[s]
            if s in hashmap:
                cache[s] = True
                return True

            for i in range(len(s)):
                word = s[:i]
                remain = s[i:]
                if word in hashmap and helper(remain):
                    cache[s] = True
                    return True
            cache[s] = False
            return False

        return helper(s)
