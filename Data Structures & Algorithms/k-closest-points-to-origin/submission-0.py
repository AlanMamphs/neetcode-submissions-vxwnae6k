import heapq
import math

class Solution:
    def distance(self, point):
        return math.sqrt(point[0]**2 + point[1]**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        for p in points:
            heapq.heappush(store, (-self.distance(p), p))
            if len(store) > k:
                heapq.heappop(store)
        return [x[1] for x in store]