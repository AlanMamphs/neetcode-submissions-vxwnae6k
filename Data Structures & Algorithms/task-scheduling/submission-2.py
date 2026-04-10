from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = []
        for x in Counter(tasks).values():
            heapq.heappush(counts, -x)
        cooldown = deque()
        time = 0
        while counts or cooldown:
            time += 1
            if not counts:
                time = cooldown[0][0]
            else:
                count = 1 + heapq.heappop(counts)
                if count:
                    cooldown.append((n + time, count))
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(counts, cooldown.popleft()[1])
        return time