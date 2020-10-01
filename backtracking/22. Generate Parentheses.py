# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left, right, temp, result, n):
            if left < right: return
            if left > n or right > n: return
            if left == n and right == n:
                result.append("".join(temp))

            temp.append('(')
            helper(left + 1, right, temp, result, n)
            temp.pop()

            temp.append(')')
            helper(left, right + 1, temp, result, n)
            temp.pop()

        result = []
        helper(0, 0, [], result, n)
        return result
