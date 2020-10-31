# https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        items = self.hashmap[key]
        l, r = 0, len(items)
        while l < r:
            m = l + (r - l) // 2
            if items[m][0] > timestamp:
                r = m
            else:
                l = m + 1
        if l == 0:
            return ""
        return items[l - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)