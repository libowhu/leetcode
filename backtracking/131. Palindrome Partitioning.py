# https://leetcode.com/problems/palindrome-partitioning/submissions/
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(s):
            if s in cache: return cache[s]

            output = []
            if s == s[::-1]:
                output.append([s])

            for i in range(1, len(s)):
                l_s = s[:i]
                r_s = s[i:]
                if l_s == l_s[::-1]:
                    ps1 = [[l_s]]
                    ps2 = helper(r_s)
                    output.extend([x + y for x in ps1 for y in ps2])
            cache[s] = output
            return output

        cache = {}
        return helper(s)
