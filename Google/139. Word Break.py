class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def breaker(target, wordDict):
            if target in cache:
                return cache[target]
            if target in wordDict:
                return True

            for idx in range(1, len(target)):
                left = target[:idx]
                right = target[idx:]
                if left in wordDict and breaker(right, wordDict):
                    cache[target] = True
                    return True

            cache[target] = False
            return False

        return breaker(s, wordDict)
