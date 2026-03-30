from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        times = self.store[key]

        l = 0
        r = len(times) - 1
        res = (0, "")
        while l <= r:
            m = l + (r - l) // 2
            if times[m][0] <= timestamp:
                res = max(res, times[m])
                l = m + 1
            else:
                r = m - 1
        return res[1]