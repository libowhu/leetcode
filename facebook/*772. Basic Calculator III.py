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
                elif c in "-+*/":
                    if sign == "+":
                        stack.append(int(num))
                    if sign == "-":
                        stack.append(-1 * int(num))
                    if sign == "*":
                        stack.append(stack.pop() * int(num))
                    if sign == "/":
                        stack.append(int(stack.pop() / int(num)))
                    sign = c
                    num = ""
                elif c in "()":
                    if c == "(":
                        num = helper(q)
                    if c == ")":
                        if sign == "+":
                            stack.append(int(num))
                        if sign == "-":
                            stack.append(-1 * int(num))
                        if sign == "*":
                            stack.append(stack.pop() * int(num))
                        if sign == "/":
                            stack.append(int(stack.pop() / int(num)))
                        break

            return sum(stack)

        s = s.replace(" ", '')
        q = collections.deque(list(s + '+'))

        return helper(q)
