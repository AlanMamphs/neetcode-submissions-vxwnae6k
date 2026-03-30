from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.store[key]
        if not timestamps:
            return ""
        
        res = (0, "")

        l = 0
        r = len(timestamps) - 1
        while l <= r:
            m = l + (r - l) // 2
            if timestamps[m][0] <= timestamp:
                res = max(timestamps[m], res, key=lambda x: x[0])
                l = m + 1
            else:
                r = m - 1

        return res[1]
