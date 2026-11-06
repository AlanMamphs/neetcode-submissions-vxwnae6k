class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_h = [-c for c in Counter(tasks).values()]
        heapq.heapify(max_h)

        dq = deque()
        time = 0
        while max_h or dq:
            time += 1
            if max_h:
                c = 1 + heapq.heappop(max_h)
                if c:
                    dq.append((c, time + n))
            
            if dq and dq[0][1] == time:
                heapq.heappush(max_h, dq.popleft()[0])
        return time