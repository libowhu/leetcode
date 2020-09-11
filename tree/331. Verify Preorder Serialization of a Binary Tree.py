# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for value in preorder.split(','):
            if value == '#':
                while len(stack) >= 2 and stack[-1] == '#' and stack[-2] != '#':
                    stack.pop()
                    stack.pop()
            stack.append(value)
        return stack == ['#']