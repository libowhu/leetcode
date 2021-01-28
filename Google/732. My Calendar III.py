class MyCalendarThree:

    def __init__(self):
        self.bookings = []
        self.hashmap = collections.defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.hashmap[start] += 1
        self.hashmap[end] -= 1

        res = temp = 0
        for key in sorted(self.hashmap.keys()):
            temp += self.hashmap[key]
            res = max(res, temp)

        return res

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
