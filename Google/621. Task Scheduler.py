# https://leetcode.com/problems/task-scheduler/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        total = len(tasks)
        counter = collections.Counter(tasks)
        task, freq = counter.most_common(1)[0]

        count = 0
        for key in counter:
            if counter[key] == freq:
                count += 1

        remain = total - count * freq
        avail = (n + 1) * (freq - 1) - count * (freq - 1)
        if avail < 0: return total
        if remain > avail:
            return (n + 1) * (freq - 1) + count + remain - avail
        else:
            return (n + 1) * (freq - 1) + count