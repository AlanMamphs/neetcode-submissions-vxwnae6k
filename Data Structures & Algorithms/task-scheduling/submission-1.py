from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-c for k, c in counts.most_common()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while max_heap or q:
            time += 1
            if not max_heap:
                time = q[0][1]
            else:
                c = heapq.heappop(max_heap) + 1
                if c:
                    q.append((c, n + time))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time