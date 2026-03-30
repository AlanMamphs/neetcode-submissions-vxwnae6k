from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        visit = {}
        minheap = [(0, k)]
        neighs = defaultdict(list)

        for ui, vi, ti in times:
            neighs[ui].append((ti, vi))
        result = 0
        while minheap:
            w1,n1 = heappop(minheap)
            if n1 in visit:
                continue
            visit[n1] = w1
            result = max(result, w1)
            for w2, n2 in neighs[n1]:
                heappush(minheap, (w1+w2, n2))
        
        return result if n == len(visit) else -1

