# https://leetcode.com/problems/my-calendar-ii/
class MyCalendarTwo:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        hashmap = collections.defaultdict(int)
        self.bookings.append([start, end])
        for booking in self.bookings:
            s, e = booking
            hashmap[s] += 1
            hashmap[e] -= 1

        res = 0
        for key in sorted(hashmap.keys()):
            res += hashmap[key]
            if res > 2:
                self.bookings.pop()
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

class MyCalendarTwo:

    def __init__(self):
        self.overlaps = []
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if max(s, start) < min(e, end):
                return False

        for s, e in self.bookings:
            if max(s, start) < min(e, end):
                self.overlaps.append([max(s, start), min(e, end)])
        self.bookings.append([start, end])
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)