# https://leetcode.com/problems/reorganize-string/
class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = collections.Counter(S)
        n = len(S)

        def helper(pre, counter, temp, count, result):
            if count == len(temp):
                result.append(temp)
                return

            for key in counter:
                if key != pre:
                    val = counter[key]
                    if val > 0:
                        counter[key] = val - 1
                        helper(key, counter, temp + key, count, result)
                        counter[key] = val

        result = []
        helper("", counter, "", n, result)
        if result:
            return result[0]
        else:
            return ""


class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = collections.Counter(S)
        heap = []
        for key in counter:
            heap.append((-counter[key], key))

        heapq.heapify(heap)
        result = ""
        while len(heap) > 1:
            count1, key1 = heapq.heappop(heap)
            count2, key2 = heapq.heappop(heap)
            if result and result[-1] == key1:
                result += key2 + key1
            else:
                result += key1 + key2
            count1 += 1
            count2 += 1
            if count1 != 0:
                heapq.heappush(heap, (count1, key1))
            if count2 != 0:
                heapq.heappush(heap, (count2, key2))

        if len(heap) == 1:
            count, key = heapq.heappop(heap)
            if count < -1 or (result and result[-1] == key):
                return ""
            else:
                result += key
        return result

