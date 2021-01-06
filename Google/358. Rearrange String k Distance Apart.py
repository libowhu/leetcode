# https://leetcode.com/problems/rearrange-string-k-distance-apart/
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s
        n = len(s)
        counter = collections.Counter(s)
        c, freq = counter.most_common(1)[0]
        result = [[] for _ in range(freq)]
        index = 0

        for key in sorted(counter, key=counter.get, reverse=True):
            count = counter[key]
            if count == freq:
                for i in range(freq):
                    result[i].append(key)
                continue
            while count != 0:
                result[index].append(key)
                index += 1
                count -= 1
                if index == freq - 1:
                    index = 0
        output = ""
        for idx, l in enumerate(result):
            if idx != freq-1 and len(l) < k:
                return ""
            for c in l:
                output += c
        return output