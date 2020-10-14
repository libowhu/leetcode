# https://leetcode.com/problems/basic-calculator/
class Solution:
    def calculate(self, s: str) -> int:
        def helper(q):
            stack = []
            num = ""
            sign = "+"

            while q:
                c = q.popleft()
                if c.isdigit():
                    num += c
                elif c in "-+":
                    if sign == "+":
                        stack.append(int(num))
                    if sign == "-":
                        stack.append(-int(num))
                    sign = c
                    num = ""
                elif c == "(":
                    num = helper(q)
                elif c == ")":
                    if sign == "+":
                        stack.append(int(num))
                    if sign == "-":
                        stack.append(-int(num))
                    break

            return sum(stack)

        s = s.replace(" ", "")
        q = collections.deque(list(s + '+'))
        return helper(q)
