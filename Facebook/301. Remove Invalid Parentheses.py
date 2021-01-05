# https://leetcode.com/problems/remove-invalid-parentheses/
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            if c == ')':
                if left != 0:
                    left -= 1
                else:
                    right += 1

        def is_valid(s):
            open = 0
            for c in s:
                if c == '(':
                    open += 1
                if c == ')':
                    if open == 0:
                        return False
                    else:
                        open -= 1
            if open == 0:
                return True
            else:
                return False

        def backtrack(s, left, right, output):
            if left == 0 and right == 0:
                if is_valid(s):
                    output.add(s)
                    return
            if right > 0:
                for i in range(len(s)):
                    c = s[i]
                    if i > 0 and s[i] == s[i - 1] == ')':
                        continue
                    if c == ')':
                        backtrack(s[:i] + s[i + 1:], left, right - 1, output)
            elif left > 0:
                for i in range(len(s)):
                    c = s[i]
                    if i > 0 and s[i] == s[i - 1] == '(':
                        continue
                    if c == '(':
                        backtrack(s[:i] + s[i + 1:], left - 1, right, output)

        output = set()
        backtrack(s, left, right, output)
        return list(output)
