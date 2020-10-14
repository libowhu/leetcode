# https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def helper(s):
            if s in memo:
                return memo[s]

            result = False
            for i in range(len(s)):
                word = s[:i + 1]
                if word in wordDict:
                    if not s[i + 1:]:
                        result = True
                        break
                    else:
                        if helper(s[i + 1:]):
                            result = True
                            break
            memo[s] = result
            return result

        return helper(s)