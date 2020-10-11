# https://leetcode.com/problems/word-break-ii/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def backtracking(s, wordDict, memo):
            if not s:
                return []

            if s in memo:
                return memo[s]

            output = []
            for i in range(len(s)):
                word = s[:i + 1]
                if word in wordDict:
                    if not s[i + 1:]:
                        output.append(word)
                        break
                    remains = backtracking(s[i + 1:], wordDict, memo)
                    if remains:
                        for remain in remains:
                            output.append(word + ' ' + remain)

            memo[s] = output
            return output

        memo = {}
        output = backtracking(s, wordDict, memo)
        return output