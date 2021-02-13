class Solution:
    def numDecodings(self, s: str) -> int:
        lookup = { '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'
        }
        cache = {}
        def backtracking(string):
            if string in cache: return cache[string]
            res = 0
            if string in lookup:
                res += 1
            for i in range(1, len(string)):
                left = string[:i]
                right = string[i:]
                if left in lookup:
                    temp = backtracking(right)
                    if temp:
                        res += temp
            cache[string] = res
            return res
        return backtracking(s)
