import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        store = []
        for s in stones:
            heapq.heappush(store, -s)
        while len(store) > 1:
            s1, s2 = heapq.heappop(store), heapq.heappop(store)
            heapq.heappush(store, -abs(s1 - s2))

        return store and -store[0] or 0
