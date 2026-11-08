class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_h = []
        for s in stones:
            heapq.heappush(max_h, -s)
        
        while len(max_h) > 1:
            stone = heapq.heappop(max_h) - heapq.heappop(max_h)
            if stone:
                heapq.heappush(max_h, stone)
        return max_h and -max_h[0] or 0