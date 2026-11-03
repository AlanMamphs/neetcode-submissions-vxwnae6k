import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        def distance(x, y):
            return math.sqrt(x**2 + y**2)
        
        for x, y in points:
            heapq.heappush(max_heap, (-distance(x, y), (x, y)))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [x[1] for x in max_heap]