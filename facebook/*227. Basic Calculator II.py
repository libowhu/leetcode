# https://leetcode.com/problems/basic-calculator-ii/
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        presign = "+"

        for c in s + "+":
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if presign == '+':
                    stack.append(num)
                if presign == '-':
                    stack.append(-num)
                if presign == '*':
                    stack.append(stack.pop() * num)
                if presign == '/':
                    stack.append(int(stack.pop() / num))
                presign = c
                num = 0

        return sum(stack)