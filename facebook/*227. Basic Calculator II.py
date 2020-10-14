# https://leetcode.com/problems/basic-calculator-ii/
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = ""
        sign = "+"
        q = collections.deque(list(s + '+'))

        while q:
            c = q.popleft()
            if c.isdigit():
                num += c
            elif c in "+-*/":
                if sign == "+":
                    stack.append(int(num))
                if sign == "-":
                    stack.append(-int(num))
                if sign == "*":
                    stack.append(stack.pop() * int(num))
                if sign == "/":
                    stack.append(int(stack.pop() / int(num)))
                sign = c
                num = ""

        return sum(stack)