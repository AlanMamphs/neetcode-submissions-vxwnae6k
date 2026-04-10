import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_h = [-x for x in stones]
        heapq.heapify(max_h)

        while len(max_h) > 1:
            x, y = heapq.heappop(max_h), heapq.heappop(max_h)

            stone = abs(x - y)
            if stone:
                heapq.heappush(max_h, -stone)
        
        return max_h and -max_h[0] or 0