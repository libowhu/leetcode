# https://leetcode.com/problems/my-calendar-i/
class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # print(start, end, self.bookings)
        for booking in self.bookings:
            cur_start, cur_end = booking
            if max(cur_start, start) < min(cur_end, end):
                return False
        self.bookings.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        left = bisect.bisect_left(self.bookings, end)
        right = bisect.bisect_right(self.bookings, start)

        if left == right and right % 2 == 0:
            self.bookings[left:right] = [start, end]
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)