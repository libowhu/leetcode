# https://leetcode.com/problems/compare-version-numbers/
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        tokens1 = version1.split('.')
        tokens2 = version2.split('.')

        if len(tokens1) > len(tokens2):
            tokens2.extend([0] * (len(tokens1) - len(tokens2)))
        if len(tokens1) < len(tokens2):
            tokens1.extend([0] * (len(tokens2) - len(tokens1)))

        for token1, token2 in zip(tokens1, tokens2):
            num1 = int(token1)
            num2 = int(token2)

            if num1 > num2:
                return 1
            if num1 < num2:
                return -1

        return 0