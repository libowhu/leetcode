# https://leetcode.com/problems/longest-string-chain/
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        result = 1

        for word in sorted(words, key=len):
            dp[word] = 1

            for i in range(len(word)):
                pre = word[:i] + word[i + 1:]

                if pre in dp:
                    dp[word] = max(dp[word], dp[pre] + 1)
                    result = max(result, dp[word])
        return result
