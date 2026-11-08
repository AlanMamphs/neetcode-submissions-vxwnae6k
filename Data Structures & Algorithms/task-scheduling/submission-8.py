class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_h = []
        for c in Counter(tasks).values():
            heapq.heappush(max_h, -c)
        time = 0
        q = deque()
        while max_h or q:
            time += 1
            if max_h:
                c = 1 + heapq.heappop(max_h)
                if c:
                    q.append((c, time + n))
            if q:
                if q[0][1] == time:
                    heapq.heappush(max_h, q.popleft()[0])
        return time 
