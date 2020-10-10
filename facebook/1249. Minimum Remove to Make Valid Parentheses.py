# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        output = []
        for c in s:
            if c == '(':
                open += 1
                output.append(c)
                continue
            if c == ')':
                if open <= 0:
                    continue
                else:
                    open -= 1
            output.append(c)

        if open == 0:
            return output
        else:
            result = []
            for c in output[::-1]:
                if c == '(':
                    if open > 0:
                        open -= 1
                        continue
                result.append(c)

        return ''.join(result[::-1])
