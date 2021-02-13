class Solution:
    def numDecodings(self, s: str) -> int:
        lookup = { '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'
        }
        cache = {}
        def backtracking(string):
            if string in cache: return cache[string]
            res = 0
            if string in lookup:
                res += 1
            for i in range(1, len(string)):
                left = string[:i]
                right = string[i:]
                if left in lookup:
                    temp = backtracking(right)
                    if temp:
                        res += temp
            cache[string] = res
            return res
        return backtracking(s)


class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(s):
            n = len(s)
            dp = [0] * (n + 1)

            dp[0] = 1
            dp[1] = 1 if s[0] != '0' else 0

            for i in range(2, n + 1):
                str1 = s[i - 1:i]
                str2 = s[i - 2:i]
                if str1 and not str1.startswith("0") and 1 <= int(str1) <= 9:
                    dp[i] += dp[i - 1]

                if str2 and not str2.startswith("0") and 10 <= int(str2) <= 26:
                    dp[i] += dp[i - 2]
            return dp[n]

        return helper(s)