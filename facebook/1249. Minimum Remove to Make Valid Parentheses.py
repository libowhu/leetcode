# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            if c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        output = []
        for c in s:
            if c == ')' and right > 0:
                right -= 1
                continue
            else:
                output.append(c)

        result = []
        for c in output[::-1]:
            if c == '(' and left > 0:
                left -= 1
                continue
            else:
                result.append(c)

        return "".join(result[::-1])
