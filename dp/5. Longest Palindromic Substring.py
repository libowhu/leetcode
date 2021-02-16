# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extendFromMiddle(s, left, right):
            res = ""
            l, r = left, right
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r + 1]) > len(res):
                        res = s[l:r + 1]
                else:
                    break
                l -= 1
                r += 1
            return res

        res = ""
        for i in range(len(s)):
            temp = extendFromMiddle(s, i, i)
            if len(temp) > len(res):
                res = temp
            temp = extendFromMiddle(s, i, i + 1)
            if len(temp) > len(res):
                res = temp

        return res
