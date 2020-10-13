# 
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        atom = ""
        num = 0
        count = 1
        elements = collections.defaultdict(int)
        digit = 0
        coff = 1

        for c in formula[::-1]:
            if c.isdigit():
                num += 10 ** digit * int(c)
                digit += 1
            elif c.isupper():
                atom += c
                count = num if num != 0 else 1
                elements[atom[::-1]] += count * coff
                atom = ""
                num = digit = 0
            elif c.islower():
                atom += c
            elif c == ')':
                count = num if num != 0 else 1
                stack.append(count)
                coff *= count
                num = count = digit = 0
            elif c == '(':
                coff //= stack.pop()
                coff = max(1, coff)
                num = count = digit = 0

        sorted_keys = sorted(elements.keys())
        output = ""
        for key in sorted_keys:
            if elements[key] == 1:
                output += key
            else:
                output += key + str(elements[key])

        return output