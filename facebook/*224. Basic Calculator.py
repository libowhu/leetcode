# https://leetcode.com/problems/basic-calculator/
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        presign = 1
        num = 0
        sum = 0

        for c in s + "+":
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                if presign == 1:
                    sum += num * 1
                if presign == -1:
                    sum += num * -1
                presign = 1 if c == "+" else -1
                num = 0
            elif c in '()':
                if c == "(":
                    stack.append((sum, presign))
                    sum = 0
                if c == ")":
                    sum += presign * num
                    pre_sum, pre_presign = stack.pop()
                    sum = pre_sum + pre_presign * sum
                num = 0
                presign = 1

        return sum