# https://leetcode.com/problems/word-break-ii/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(s):
            if s in memo:
                return memo[s]

            output = []
            for i in range(len(s)):
                word = s[:i + 1]
                if word in wordDict:
                    if not s[i + 1:]:
                        output.append([word])
                    else:
                        word_lists = helper(s[i + 1:])
                        for word_list in word_lists:
                            output.append([word] + word_list)
            memo[s] = output
            return output

        memo = {}
        result = []
        combs = helper(s)
        for comb in combs:
            result.append(" ".join(comb).strip())
        return result
