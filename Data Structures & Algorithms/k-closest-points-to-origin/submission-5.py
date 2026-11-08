class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_h = []

        for x, y in points:
            heapq.heappush(max_h, (-(x**2 + y**2), (x, y)))
            if len(max_h) > k:
                heapq.heappop(max_h)
        return [x[1] for x in max_h]