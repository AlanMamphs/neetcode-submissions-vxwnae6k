class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_h = []

        for a in arr:
            heapq.heappush(min_h, (abs(a - x), a))

        res = []
        for i in range(k):
            res.append(heapq.heappop(min_h)[1])
        res.sort()
        return res