# https://leetcode.com/problems/number-of-atoms/
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def helper(q):
            result = collections.defaultdict(int)
            atom = ""
            num = ""

            while q:
                c = q.popleft()
                if c.isupper() or c == "#":
                    if atom:
                        result[atom] += int(num or 1)
                    atom = c
                    num = ""
                if c.islower():
                    atom += c
                if c.isdigit():
                    num += c
                if c == "(":
                    temp = helper(q)
                    temp_num = ""
                    if q and q[0].isdigit():
                        while q and q[0].isdigit():
                            temp_num += q.popleft()
                    for key in temp:
                        result[key] += temp[key] * int(temp_num or 1)
                if c == ")":
                    if atom:
                        result[atom] += int(num or 1)
                    break
            return result

        q = collections.deque(list(formula + '#'))
        mapper = helper(q)
        sorted_keys = sorted(mapper.keys())
        result = ""
        for key in sorted_keys:
            if mapper[key] == 1:
                result += key
            else:
                result += key + str(mapper[key])
        return result